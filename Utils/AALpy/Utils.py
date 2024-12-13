import itertools
import random
from dataclasses import dataclass
from typing import Any

import numpy as np
import numpy.typing as npt
from scipy.sparse.csgraph import shortest_path

from Utils.CustomKeyDict import CustomKeyDict
from Utils.GeneralUtils import count_from_to, filter_dict
from aalpy import DeterministicAutomaton, save_automaton_to_file
from aalpy.base import AutomatonState, Automaton

def visualize(automaton, path):
  dot_string = save_automaton_to_file(automaton, file_type="string")
  with open(path, "w") as file:
    file.write(dot_string)

def sample_target_state_prefixes(
    model : Automaton, target_states : list[AutomatonState] = None, initial_state = None,
    max_depth = 20, prefixes_per_state = 3
) -> dict[AutomatonState, list[list]]:
  """
  Samples traces from the model which end in one of the target states with different lengths.

  :param model: the automaton from which to sample
  :param target_states: list of states in which to end.
         if `None` is provided, this is set of all states.
  :param initial_state: state from which to start the search.
         if `None` is provided, this is set to the initial state of the model
  :param max_depth: maximal length of returned traces.
  :param prefixes_per_state: limits the number of prefixes of a given length per state to combat combinatorial explosion.

  :return: dict mapping target states to a list of prefixes
  """

  if initial_state is None:
    initial_state = model.initial_state
  if target_states is None:
    target_states = model.states

  # search_dict maps states to a structure containing valid prefixes of the state
  # this structure is a nested list where
  # - the first index corresponds to the number of steps
  # - the resulting list contains up to `prefix_per_state` many prefixes which are themselves lists.
  search_dict: dict[AutomatonState, list[list[list]]]
  search_dict = {state: [[] for _ in range(max_depth)] for state in model.states}
  search_dict[initial_state][0].append([])

  for depth in range(1, max_depth):
    for state, grouped_prefixes in search_dict.items():
      prefixes = grouped_prefixes[depth - 1]
      if len(prefixes) == 0:
        continue
      for in_sym in model.get_input_alphabet():
        search_dict[state.transitions[in_sym]][depth].extend([p + [in_sym] for p in prefixes])

    for state, grouped_prefixes in search_dict.items():
      prefixes = grouped_prefixes[depth]
      if prefixes_per_state < len(prefixes):
        grouped_prefixes[depth] = random.sample(prefixes, prefixes_per_state)

  return {state: list(itertools.chain(*search_dict[state])) for state in target_states}

def upstream(model : Automaton, states : list[AutomatonState], count = None) -> dict[AutomatonState, list]:
  """
  Computes which states can reach a given set of states `states` in at most `count` steps
  :return: A dictionary mapping states to one of the shortest paths.
  """
  reached = [{state : None for state in states}]
  remaining = set(model.states) - reached[-1].keys()

  for length in count_from_to(1, count):
    new_states = dict()
    for state in list(remaining):
      for in_sym, target_state in state.transitions.items():
        if target_state in reached[-1]:
          remaining.discard(state)
          new_states[state] = (in_sym, target_state)
    if len(new_states) == 0:
      break
    reached.append(new_states)

  ret = {state : [] for state in reached[0].keys()}
  for r in reached[1:]:
    for state, (in_sym, target_state) in r.items():
      ret[state] = [in_sym] + ret[target_state]

  return ret

def upstream_distance_sets(model : Automaton, s1 : list[AutomatonState], s2 : list[AutomatonState]) -> tuple[int, set[AutomatonState]]:
  reached = [set(s1), set(s2)]
  remaining = set(model.states) - set.union(*reached)

  prev_len = len(remaining)

  for len in count_from_to(0):
    inter = set.intersection(*reached)
    if len(inter) != 0:
      return len, inter

    for state in remaining:
      for next_state in state.transitions.values():
        for r in reached:
          if next_state in r:
            r.add(state)
            remaining.discard(state)

    current_len = len(remaining)
    if current_len == prev_len:
      return None, set()
    prev_len = current_len

def upstream_distance_matrix(model : Automaton, states_to_eval : list[AutomatonState] = None) -> npt.ArrayLike:
  if states_to_eval is None:
    states_to_eval = model.states
  n = len(states_to_eval)

  @dataclass
  class Info:
    upstream_dict : dict[AutomatonState, int]
    final : bool

  infos = [Info({state : 0}, False) for state in states_to_eval]
  distance = np.inf * np.ones((n, n))
  distance[np.eye(n, dtype=bool)] = 0
  to_check = {(idx1, idx2) for idx1 in range(n) for idx2 in range(idx1+1, n)}
  for length in count_from_to(1):
    new_states = []
    for info in infos:
      new_set = set()
      new_states.append(new_set)
      if info.final:
        continue
      for us_state in model.states:
        if us_state in info.upstream_dict:
          continue
        if any(child in info.upstream_dict for child in us_state.transitions.values()):
          info.upstream_dict[us_state] = length
          new_set.add(us_state)
      info.final = len(new_set) == 0

    checked = []
    for s1, s2 in to_check:
      o1, o2 = infos[s1].upstream_dict, infos[s2].upstream_dict
      n1, n2 = new_states[s1], new_states[s2]

      if len(set.intersection(n1, n2)) != 0 or len(set.intersection(n2, o1)) != 0 or len(set.intersection(n1, o2)) != 0:
        checked.append((s1, s2))
        distance[s1, s2] = length
        distance[s2, s1] = length

    to_check.difference_update(checked)
    if len(to_check) == 0 or all(info.final for info in infos):
      return distance

def downstream(states : list[AutomatonState], count) -> dict[AutomatonState, tuple[AutomatonState, Any, ...]]:
  """
  Computes which states can be reached from a given set of states `states` in at most `count` steps.
  :return: A dictionary mapping each state to any of its shortest access sequences.
           This is given as a tuple containing the initial state followed by input symbols.
  """
  reached = [{state : None for state in states}]

  for length in count_from_to(1, count):
    new_states = dict()
    for state in reached[-1].keys():
      for in_sym, target_state in state.transitions.items():
        if all(target_state not in x for x in reached):
          new_states[target_state] = state, in_sym
    if len(new_states) == 0:
      break
    reached.append(new_states)

  ret = {state : (state,) for state in states}
  for r in reached[1:]:
    for state, (prev_state, in_sym) in r.items():
      ret[state] = ret[prev_state] + (in_sym,)

  return ret

def downstream_distance_matrix(model: DeterministicAutomaton, src_states : list[AutomatonState] = None, compute_policy = False):
  n = len(model.states)
  state_map = {state: idx for idx, state in enumerate(model.states)}
  direct_dist = np.zeros((n,n)) # it seems dijkstra also accepts 0 as inf # TODO use sparse matrix
  for src_idx, src in enumerate(model.states):
    for dst in src.transitions.values():
      direct_dist[src_idx, state_map[dst]] = 1

  if src_states is not None:
    src_states = [state_map[state] for state in src_states]

  distance_mat, predecessors = shortest_path(direct_dist, unweighted=True, return_predecessors=True, indices=src_states)

  # enforce leaving the state
  for idx_src in range(n):
    potential_indices = list(filter(lambda x: direct_dist[x, idx_src], range(n)))
    if len(potential_indices) == 0:
      distance_mat[idx_src, idx_src] = np.inf
      continue
    best_idx = min(potential_indices, key=lambda x: distance_mat[idx_src, x])
    distance = distance_mat[idx_src, best_idx]
    if distance == np.inf:
      distance_mat[idx_src, idx_src] = np.inf
      continue
    distance_mat[idx_src, idx_src] = distance + 1
    predecessors[idx_src, idx_src] = best_idx

  if not compute_policy:
    return distance_mat

  policy = CustomKeyDict()
  # TODO this is inefficient but can't seem to find a nice solution that has a good runtime complexity but does not melt my brain
  for src_idx, src_predecessors in enumerate(predecessors):
    src_state = model.states[src_idx]
    local_policy = policy[src_state] = CustomKeyDict()

    for dst_idx, pred_idx in enumerate(src_predecessors):
      if pred_idx < 0:
        continue
      current_idx = dst_idx
      while not direct_dist[src_idx, current_idx] == 1:
        current_idx = src_predecessors[current_idx]

      current_state = model.states[current_idx]
      dst_state = model.states[dst_idx]
      symbol = [sym for sym, succ in src_state.transitions.items() if succ is current_state][0]
      local_policy[dst_state] = symbol

  return distance_mat, policy

def between(src : list[AutomatonState], dst : list[AutomatonState], count = None):
  """
  Compute the set of states which are along possible paths between a set of source and destination states.
  :return: A dict mapping each state to a tuple comprised of a possible access sequence and a possible path to a destination state
  """
  backward = downstream(src, count)
  to_check = {state : len(access) - 1 for state, access in backward.items() if state not in dst}
  forward = [{state : None for state in backward.keys() if state in dst}]

  for len_path_from in count_from_to(1, count):
    targets = forward[-1]
    next_fwd = dict()
    checked = []
    for state, len_path_to in to_check.items():
      if count is not None and count < len_path_to + len_path_from:
        checked.append(state)
        continue
      for in_sym, next_state in state.transitions.items():
        if next_state in targets:
          next_fwd[state] = (in_sym, next_state)
          checked.append(state)
          break
    for td in checked:
      del to_check[td]
    if len(next_fwd) == 0:
      break
    forward.append(next_fwd)

  ret_fwd = {state : [] for state in forward[0].keys()}
  for fwd in forward[1:]:
    for state, (in_sym, next_state) in fwd.items():
      ret_fwd[state] = [in_sym] + ret_fwd[next_state]

  return {state : (backward[state], fwd) for state, fwd in ret_fwd.items()}

def restrict_to_states(model : Automaton, states : list[AutomatonState]) -> Automaton:
  ids = {state.state_id for state in states}
  new_model = model.copy()
  new_model.states = list(filter(lambda x: x.state_id in ids, new_model.states))
  for state in new_model.states:
    state.transitions = filter_dict(lambda in_sym, n_state: n_state.state_id in ids, state.transitions)

  return new_model
