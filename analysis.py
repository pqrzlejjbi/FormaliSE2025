import itertools
import random

import numpy as np
from aalpy import visualize_automaton, make_input_complete, convert_i_o_traces_for_RPNI
from aalpy.learning_algs.deterministic_passive.rpni_helper_functions import createPTA

from Utils.OpenScenario.Simulation.SimulationGUI import SimulationControlGUI
from Utils.AALpy.Utils import upstream_distance_matrix, between, downstream, restrict_to_states, \
  sample_target_state_prefixes
from Utils.NumpyUtils import minimal_maximal_cost_structure
from Utils.FileUtils import OutputDataManagement as odm

from scenario_definition import SinkState, get_sul


def analyze_traces(traces, target_outputs):
  dom_viols = {ss: 0 for ss in SinkState if ss}
  for trace in traces:
    for _, o in trace:
      if o in dom_viols:
        dom_viols[o] += 1
        break

  pta = createPTA(convert_i_o_traces_for_RPNI(traces), "moore")
  node_queue = [pta]
  nodes = []
  uncached_traces = []
  while node_queue:
    node = node_queue.pop()
    nodes.append(node)

    if node.output in SinkState:
      node.children.clear()
    for child in node.children.values():
      node_queue.append(child)

    if len(node.children) == 0:
      current = pta
      out_seq = []
      for in_sym in node.prefix:
        current = current.children[in_sym]
        out_seq.append(current.output)

      uncached_traces.append(list(zip(node.prefix, out_seq)))

  trace_lengths = list(map(len, traces))

  result = {
    "nr traces": len(traces),
    "nr traces (c)": sum(any(o in target_outputs for i, o in trace) for trace in traces),
    "nr steps": sum(trace_lengths),
    "nr steps (c)": sum(sum(o in target_outputs for i, o in trace) for trace in traces),
    "nr uncached traces": len(uncached_traces),
    "nr uncached traces (c)": sum(any(o in target_outputs for i, o in trace) for trace in uncached_traces),
    "nr uncached steps": sum(map(len, uncached_traces)),
    "nr uncached steps (c)": sum(sum(o in target_outputs for i, o in trace) for trace in uncached_traces),
    "nr unique steps": len(nodes),
    "nr unique steps (c)": sum(node.output in target_outputs for node in nodes),
    "trace length (avg)": sum(trace_lengths)/len(traces),
    "trace length (max)": max(trace_lengths),
  }
  result.update(**dom_viols)
  return result

def analyze_model(model, name, target_outputs, is_critical=None):

  visualize_automaton(model, odm.get_path(path=name), "dot")

  print(f"model outputs: {set(state.output for state in model.states)}")

  if is_critical is None:
    def is_critical(state):
      return state.output in target_outputs
  critical_states = list(filter(is_critical, model.states))
  print(f"Model contains {len(critical_states)} state(s) with the target output(s) amongst {len(model.states)}")
  if len(critical_states) == 0:
    return

  mat = upstream_distance_matrix(model, critical_states)
  dendrogram = minimal_maximal_cost_structure(mat)
  l = [dendrogram]
  clusters = []
  while len(l) != 0:
    node = l.pop()
    if node.distance <= 2:
      clusters.append(node)
    else:
      l.extend(node.children)
  print("clusters of critical states:")
  for cluster in clusters:
    print(cluster.distance, [critical_states[idx].state_id for idx in cluster.nodes])

  relevant_states = set(between([model.initial_state], critical_states, None).keys())
  relevant_states.update(downstream(critical_states, 1).keys())

  if len(relevant_states) != 0:
    reduced_model = restrict_to_states(model, list(relevant_states))
    make_input_complete(reduced_model, "sink_state")
    visualize_automaton(reduced_model, odm.get_path(path = "reduced " + name), "dot")


def sample_critical_traces(model, sul, target_outputs, max_depth=20, prefixes_per_state=3, max_nr_seq_to_test = np.inf, max_nr_to_vis = 0):
  # Search for new critical traces
  target_states = [state for state in model.states if state.output in target_outputs]
  assumed_critical_traces = sample_target_state_prefixes(model, target_states, max_depth=max_depth, prefixes_per_state=prefixes_per_state)

  assumed_critical_traces = list(itertools.chain(*assumed_critical_traces.values()))
  print(f"Generated {len(assumed_critical_traces)} critical trace(s) with length up to {max_depth}")

  if max_nr_seq_to_test < len(assumed_critical_traces):
    assumed_critical_traces = random.sample(assumed_critical_traces, k=max_nr_seq_to_test)
  valid_critical_traces = []
  for t in assumed_critical_traces:
    for output in sul.query(t):
      if output in target_outputs:
        valid_critical_traces.append(t)
        break
      if output in SinkState:
        break
  print(f"Found {len(valid_critical_traces)} valid trace(s) among {len(assumed_critical_traces)} tested")

  # visualize
  nr_traces = min(len(valid_critical_traces), max_nr_to_vis)
  if nr_traces != 0:
    viz_sul = get_sul(None)
    viz_sul.original_sul.set_visualize(True)
    selection = random.sample(valid_critical_traces, nr_traces)
    SimulationControlGUI.run_queries(viz_sul, selection)

  print()