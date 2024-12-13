import random

from Utils.AALpy.SULs.CacheTree import Node, CacheTree
from Utils.AALpy.SULs.SinkStateCacheTree import SinkStateCacheTree
from Utils.AALpy.SULs.WrappingSUL import WrappingSUL
from Utils.FileUtils import PickledValue

def sampling(sul: WrappingSUL, alphabet, nr_samples, sample_len, sink_states = None, cache: PickledValue[SinkStateCacheTree] = None, checkpoint_interval=100):
  if sink_states is None:
    sink_states = []

  samples = []
  pta = SinkStateCacheTree(list(sink_states))

  dead_end_detection = CacheTree()
  dead_end_detection.root_node.value = True

  while len(samples) < nr_samples:
    idx = len(samples)
    print(f"obtained {idx+1}/{nr_samples} random samples.", end="")
    if cache:
      print(f" progress till next checkpoint {(idx % checkpoint_interval)+1}/{checkpoint_interval}", end="")
      if idx % checkpoint_interval == 0:
        cache.save()
    print("", end="\r")

    in_seq = []
    out_seq = []

    sul.pre()

    valid_sample = True
    current_node = pta.root_node
    dead_end_detection.reset()
    if dead_end_detection.root_node.value != True:
      raise ValueError("Could not find any more samples")

    for _ in range(sample_len):
      # check actions that don't lead to sink
      legal = []
      for in_sym in alphabet:
        sink_state_not_immanent = in_sym not in current_node.children or current_node.children[in_sym].value not in sink_states
        dead_end_not_immanent = dead_end_detection.lookup(in_sym) in [dead_end_detection.missing, True]
        if sink_state_not_immanent and dead_end_not_immanent:
          legal.append(in_sym)

      # if all actions lead to known sink, we need to abort
      if len(legal) == 0:
        valid_sample = False
        dead_end_detection.curr_node.value = False
        break

      in_sym = random.choice(legal)
      out_sym = sul.step(in_sym)

      in_seq.append(in_sym)
      out_seq.append(out_sym)

      if in_sym not in current_node.children:
        current_node.children[in_sym] = Node(out_sym)
      current_node = current_node.children[in_sym]
      dead_end_detection.insert_step(in_sym, True)

      if out_sym in sink_states:
        break

    sul.post()
    if valid_sample:
      samples.append((in_seq, out_seq))

  # some checks
  assert sum(len(set(outs[:-1]).intersection(sink_states)) != 0 for ins, outs in samples) == 0
  setified = set(tuple(zip(in_seq, out_seq)) for in_seq, out_seq in samples)
  if len(setified) != nr_samples:
    print(f"generated {nr_samples - len(setified)} duplicates")

  if cache:
    cache.save()

  return [list(zip(i,o)) for i,o in samples]