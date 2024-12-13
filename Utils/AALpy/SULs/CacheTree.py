from pathlib import Path
from queue import Queue
from typing import Dict, Iterable, Any

from Utils.FileUtils import load, dump
from aalpy.automata import MooreState, MooreMachine

class CacheInterface:
  missing = object()
  def __init__(self):
    self.inputs = []
    self.outputs = []

  def reset(self):
    self.inputs = []
    self.outputs = []

  def insert(self, input, output):
    ...

  def lookup(self, input) -> Any:
    ...

  def step(self, input):
    ...

  def lookup_step(self, input):
    out = self.lookup(input)
    if not (out is self.missing):
      self.step(input)
    return out

  def insert_step(self, input, output):
    self.insert(input, output)
    self.step(input)

  def insert_seq(self, input_seq : tuple, output_seq : tuple, check : bool = True):
    self.reset()
    for inp, out in zip(input_seq, output_seq):
      self.insert_step(inp, out)

  def lookup_seq(self, input_seq: Iterable):
    """
    Check if the result of the membership query for input_seq is cached is in the tree. If it is, return the
    corresponding output sequence.

    Args:
        input_seq: corresponds to the membership query

    Returns:
        outputs associated with inputs if it is in the query, None otherwise
    """

    self.reset()
    for letter in input_seq:
      if self.lookup_step(letter) is self.missing:
        return None
    return self.outputs


class Node(object):
  __slots__ = ['value', 'children']

  def __init__(self, value=None):
    self.value = value
    self.children: Dict[Any, Node] = dict()

class CacheTree(CacheInterface):
  """
  Tree in which all membership queries and corresponding outputs/values are stored. Membership queries update the tree
  and while updating, check if determinism is maintained.
  Root node corresponds to the initial state, and from that point on, for every new input/output pair, a new child is
  created where the output is the value of the child, and the input is the transition leading from the parent to the
  child.
  """

  def __init__(self):
    super().__init__()
    self.root_node: Node = Node()
    self.curr_node: Node = self.root_node

  def reset(self):
    super().reset()
    self.curr_node = self.root_node

  def step(self, inp):
    new_node = self.curr_node.children.get(inp, None)
    if new_node is None:
      raise ValueError("Tried to step to missing child")
    self.curr_node = new_node
    self.inputs.append(inp)
    self.outputs.append(new_node.value)

  def insert(self, inp, out):
    """
    Preform a step in the cache. If output exist for the current state, and is not the same as `out`, throw
    the non-determinism violation error and abort learning.
    Args:

        inp: input
        out: output
    """

    node = self.curr_node.children.get(inp, None)
    if node is None:
      node = Node(out)
      self.curr_node.children[inp] = node
    elif node.value != out:
      expected_seq = list(self.outputs[:-1])
      expected_seq.append(node.value)
      msg = f'Non-determinism detected.\n' \
            f'Error inserting: {self.inputs}\n' \
            f'Conflict detected: {node.value} vs {out}\n' \
            f'Expected Output: {expected_seq}\n' \
            f'Received output: {self.outputs}'
      raise ValueError(msg)

  def lookup(self, inp):
    if inp not in self.curr_node.children:
      return self.missing
    return self.curr_node.children[inp].value

  def get_sequences(self, input_only=False):
    q = Queue[tuple[tuple, Node]]()
    q.put((tuple(), self.root_node))
    while not q.empty():
      prefix, node = q.get()
      if len(node.children) == 0:
        yield prefix
        continue
      for in_sym, next_node in node.children.items():
        next_val = in_sym if input_only else (in_sym, next_node.value)
        q.put((prefix + (next_val,), next_node))

  def visualize(self, path, file_type="pdf"):
    initial_state = MooreState("s0", self.root_node.value)
    idx = 1
    states = [initial_state]

    q = Queue[tuple[Node, MooreState]]()
    q.put((self.root_node, initial_state))
    while not q.empty():
      node, state = q.get()
      for in_sym, next_node in node.children.items():
        next_state = MooreState(f"s{idx}", next_node.value)
        q.put((next_node, next_state))
        states.append(next_state)
        idx += 1

    mm = MooreMachine(initial_state, states)
    mm.visualize(path, file_type)

# TODO: split hierarchic cache structure and persistent cache
# TODO: check whether this actually works...
class PersistentCacheTree(CacheInterface):
  def __init__(self, base_path: Path):
    super().__init__()
    self.cache = CacheTree()
    self.base_path = Path(base_path)
    self.current_path = Path(base_path)

  def reset(self):
    super().reset()
    self.cache.reset()
    self.current_path = Path(self.base_path)

  def lookup(self, input):
    value = self.cache.lookup(input)
    value_path = self.current_path / str(input) / "value"

    if value is self.missing:
      if not value_path.is_file():
        return self.missing
      value = load(value_path)
      self.cache.insert(input, value)
    return value

  def insert(self, input, output):
    self.cache.insert(input, output)

    new_path = self.current_path / str(input)
    new_path.mkdir(exist_ok=True)
    dump(new_path / "value", output)

  def step(self, input):
    self.cache.step(input)
    self.current_path = self.current_path / str(input)
