import pickle
import random
import sys
from typing import Any, Iterable

from aalpy import MooreState, MooreMachine, StatePrefixEqOracle, Automaton, run_Lstar, SUL, run_RPNI, \
  convert_i_o_traces_for_RPNI

from Utils.AALpy.Oracles.EarlyAcceptOracle import EarlyAcceptOracle
from Utils.AALpy.Utils import downstream_distance_matrix
from Utils.CustomKeyDict import CustomKeyDict
from Utils.FileUtils import PickleCache

cop = PickleCache.get_default()

def learn_model(sul, alphabet, automaton_type, max_iter, max_states, max_depth, cache = None):
  eq_oracle = StatePrefixEqOracle(alphabet, sul, walks_per_state=50, walk_len=10)

  callback = cache.save if cache else lambda: None

  def accept_cond(hyp : Automaton):
    if max_states is not None and max_states < len(hyp.states):
      print("accept early: large state space")
      return True
    if max_depth is not None and max_depth < max(len(state.prefix) for state in hyp.states):
      print("accept early: deep automaton")
      return True
    return False
  eq_oracle = EarlyAcceptOracle(accept_cond, eq_oracle, callback)

  return run_Lstar(alphabet, sul, eq_oracle=eq_oracle, automaton_type=automaton_type, max_learning_rounds=max_iter)

def compute_partition(model: MooreMachine, pta: MooreState):
  pta_to_model = CustomKeyDict[MooreState, MooreState]()
  model_to_pta = CustomKeyDict[MooreState, list[MooreState]]()

  queue = [(pta, model.initial_state)]
  while queue:
    (pta_state, model_state) = queue.pop()
    pta_to_model[pta_state] = model_state
    if model_state not in model_to_pta:
      model_to_pta[model_state] = [pta_state]
    else:
      model_to_pta[model_state].append(pta_state)

    for in_sym, next_pta_state in pta_state.transitions.items():
      next_model_state = model_state.transitions[in_sym]
      queue.append((next_pta_state, next_model_state))

  return model_to_pta, pta_to_model

def add_to_pta(pta: MooreState, trace: Iterable[tuple]):
  # TODO create counts according to GSM pta node
  pta_state = pta
  for (in_sym, out_sym) in trace:
    if in_sym not in pta_state.transitions:
      new_state = MooreState("", out_sym)
      new_state.count = 0
      new_state.prefix = pta_state.prefix + [in_sym]
      pta_state.transitions[in_sym] = new_state
    else:
      new_state = pta_state.transitions[in_sym]
      if new_state.output != out_sym:
        raise ValueError("non-det system...")
    pta_state.count += 1
    pta_state = new_state

def learn_model_ap(sul: SUL, alphabet, samples_per_round, rounds, output_weights: dict[Any, float], cache=None):
  initial_output = "init"
  pta = MooreState("", initial_output)
  pta.count = 0
  pta.prefix = []

  state = MooreState("s0", initial_output)
  state.transitions = {x : state for x in alphabet}
  model = MooreMachine(state, [state])

  pta_to_model: CustomKeyDict[MooreState, MooreState]
  model_to_pta: CustomKeyDict[MooreState, list[MooreState]]
  under_explored_dict: CustomKeyDict[MooreState, dict[Any, list[MooreState]]]
  policy: CustomKeyDict[MooreState, CustomKeyDict[MooreState, Any]]
  states_by_output: dict[Any, list[MooreState]]
  states_with_missing_inputs: list[tuple[MooreState, Any]]

  output_weights = dict(sorted(output_weights.items(), key=lambda pair: pair[1], reverse=True))
  if initial_output not in output_weights:
    output_weights[initial_output] = min(output_weights.values()) * 0.1

  def mark_under_explored_done(state, symbol, node: MooreState):
    state_dict = under_explored_dict[state]
    node_list = state_dict[symbol]
    node_list.remove(node)

    if len(node_list) != 0:
      return
    del state_dict[symbol]
    if len(state_dict) != 0:
      return
    del under_explored_dict[state]

  # sampling strategies:
  # exploit
  # - random state + path to one of the states with the most critical label so far (idea: similar paths may also yield good results)
  # - random state in set of most critical label + random walk (idea: maybe we can get even more critical)
  # explore
  # - loop through states. get corresponding pta nodes that are under-explored. add random paths (idea: state coverage)
  # - breadth first search for under-explored nodes. (idea: guarantee basic exploration initial state)
  # - missing inputs in states that are not input enabled. (idea: input completeness is nice...)
  # all sampling strategies should choose states as starting points where there is still something to explore
  def sample_random_state_to_critical():
    while len(under_explored_dict) != 0:
      state, ued = random.choice(list(under_explored_dict.items()))
      symbol, nodes = random.choice(list(ued.items()))
      node = random.choice(nodes)

      if symbol not in state.transitions:
        continue
      current_state = state.transitions[symbol]
      target_state = None
      for target_output in output_weights.keys():
        candidate_states = [t_state for t_state in states_by_output.get(target_output, []) if t_state in policy[current_state]]
        if len(candidate_states) == 0:
          continue
        target_state = random.choice(candidate_states)
        break
      if target_state is None:
        continue

      input_seq = list(node.prefix)
      input_seq.append(symbol)
      while current_state is not target_state:
        p_symbol = policy[current_state][target_state]
        input_seq.append(p_symbol)
        current_state = current_state.transitions[p_symbol]

      mark_under_explored_done(state, symbol, node)
      return input_seq
    return False

  def sample_critical_state_random_suffix():
    suffix_len = 10

    outputs, weights = [list(x) for x in zip(*output_weights.items())]
    while len(outputs) != 0:
      output_idx = random.choices(list(range(len(outputs))), weights, k=1)[0]
      potential_states = states_by_output.get(outputs[output_idx], [])
      potential_states = [state for state in potential_states if state in under_explored_dict]
      if len(potential_states) == 0:
        del outputs[output_idx]
        del weights[output_idx]
        continue

      state = random.choice(potential_states)
      symbol, nodes = random.choice(list(under_explored_dict[state].items()))
      node = random.choice(nodes)

      mark_under_explored_done(state, symbol, node)

      input_seq = list(node.prefix)
      input_seq.append(symbol)
      input_seq.extend(random.choices(alphabet, k=suffix_len-1))
      return input_seq
    return False

  def sample_missing_inputs():
    suffix_len = 10
    if len(states_with_missing_inputs) == 0:
      return False
    state, sym = random.choice(states_with_missing_inputs)
    node = random.choice(model_to_pta[state])
    input_seq = list(node.prefix)
    input_seq.append(sym)
    input_seq.extend(random.choices(alphabet, k=suffix_len-1))
    return input_seq

  def sample_random_state_plus_suffix():
    suffix_length = 10
    state = random.choice(model.states)
    nodes = model_to_pta[state]
    node_weights = [1/max(0.5, node.count) for node in nodes]
    node = random.choices(nodes, node_weights, k=1)[0]
    input_seq = list(node.prefix)
    input_seq.extend(random.choices(alphabet, k=suffix_length))
    return input_seq

  sampling_methods = [
    (1, sample_random_state_to_critical),
    (1, sample_critical_state_random_suffix),
    (1, sample_missing_inputs),
    (1, sample_random_state_plus_suffix)
  ]

  data = []

  for round_idx in range(rounds):
    model_to_pta, pta_to_model = compute_partition(model, pta)
    under_explored_dict = CustomKeyDict()
    for state, nodes in model_to_pta.items():
      ued = dict()
      for x in alphabet:
        ue = [node for node in nodes if x not in node.transitions]
        if len(ue) != 0:
          ued[x] = ue
      if len(ued) != 0:
        under_explored_dict[state] = ued

    _, policy = downstream_distance_matrix(model, compute_policy=True)
    states_with_missing_inputs = [(state, sym) for state in model.states for sym in alphabet if sym not in state.transitions]

    states_by_output = dict()
    for state in model.states:
      states = states_by_output.get(state.output, [])
      states.append(state)
      states_by_output[state.output] = states

    method_weights, current_methods = [list(x) for x in zip(*sampling_methods)]
    drawn_samples = 0
    while drawn_samples != samples_per_round:
      print(f"drawing sample {drawn_samples+1}/{samples_per_round} of round {round_idx+1}/{rounds}")#       ", end="\r")
      method_idx = random.choices(list(range(len(current_methods))), weights=method_weights, k=samples_per_round)[0]
      input_seq = current_methods[method_idx]()
      if input_seq:
        output_seq = sul.query(input_seq)
        trace = list(zip(input_seq, output_seq))
        add_to_pta(pta, trace)
        data.append(trace)
        drawn_samples += 1
      else:
        del current_methods[method_idx]
        del method_weights[method_idx]

    if cache:
      cache.save()

    @cop("RPNI")
    def learn(data):
      data = convert_i_o_traces_for_RPNI(data)
      data.append((tuple(), initial_output))
      return run_RPNI(data, "moore")
    print(f"learning model in round {round_idx+1}/{rounds}", end="\r")
    model = learn(data)
    model = pickle.loads(pickle.dumps(model)) # get "canonical" representation
  model.make_input_complete()
  return model