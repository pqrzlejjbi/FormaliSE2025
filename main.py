import random

from aalpy import MooreMachine

from Utils.OpenScenario.Simulation.SimulationGUI import SimulationControlGUI
from Utils.AALpy.SULs.SinkStateCacheTree import SinkStateCacheTree
from Utils.AALpy.SULs.WrappingSUL import TrackingSUL
from Utils.FileUtils import OutputDataManagement as odm, PickledValue, PickleCache

cop = PickleCache.get_default()
cop.add_folder("cache")

from scenario_definition import *

from learning import learn_model, learn_model_ap
from random_sampling import sampling
from analysis import analyze_model, analyze_traces, sample_critical_traces

odm = odm.get_default()

def visualize_traces(traces):
  sul = get_sul(None)
  sul.original_sul.set_visualize(True)
  SimulationControlGUI.run_queries(sul, traces)

class Methods:
  Random = "Random"
  Active = "Active"
  ActivePassive = "ActivePassive"

def run_method(method, seed) -> tuple[TrackingSUL, MooreMachine, dict]:
  random.seed(seed)
  cache = PickledValue(cop.base_path / f"seed={seed}" / f"method={method}" / "traces", lambda: SinkStateCacheTree(list(SinkState)), ["insert"])
  sul = TrackingSUL(get_sul(cache.value))
  model = None

  run_stats = dict(method=method, seed=seed)

  if method == Methods.Random:
    print("obtaining random samples")
    params=dict(nr_samples = 15000, sample_len = 20)
    samples = sampling(sul, alphabet, sink_states=SinkState, cache=cache, checkpoint_interval=100, **params)
    run_stats["nr model states"] = "-"
  elif method == Methods.ActivePassive:
    output_weights = {
      "far": 1,
      "close": 3,
      "critical": 5,
      "too close": 4,
    }
    for sink in SinkState:
      output_weights[sink] = 0.1
    params = dict(samples_per_round=100, rounds=40, output_weights=output_weights)
    print(method, params)
    model = learn_model_ap(sul, alphabet, cache=cache, **params)
    cache.save()
    model.make_input_complete()
    run_stats["nr model states"] = len(model.states)
  elif method == Methods.Active:
    params = dict(
      automaton_type = "moore",
      max_iter=15,
      max_states=200,
      max_depth=None,
    )
    print(method, params)
    model = learn_model(sul, alphabet, cache=cache, **params)
    cache.save()
    run_stats["nr model states"] = len(model.states)
  else:
    raise ValueError(f"Invalid Method {method}")

  run_stats.update(analyze_traces(sul.io_sequences, target_outputs))

  if model:
    model.visualize(odm.get_path(path=f"learned".replace(".", ",")), file_type="dot")
    print(f"model with {len(model.states)} states learned")

  return sul, model, run_stats

if __name__ == '__main__':

  learn = True
  if learn:
    analyze = False

    method = Methods.ActivePassive
    seed = 0
    sul, model, data = run_method(method, seed)

    for k, v in data.items():
      print(k, v)

    if analyze:
      analyze_model(model, f"{seed} {method}", target_outputs)
      sample_critical_traces(model, sul, target_outputs, max_nr_to_vis=10)
  else:
    traces_to_visualize = [
      # Provoke front collision
      [AccelerationAction(-5)] + [AccelerationAction(0)] * 3 + [LaneChangeAction.Right] + [
        AccelerationAction(-10)] * 7 + [AccelerationAction(0)] * 5,
      # Provoke lane invasions
      # [AccelerationAction(-10)] + [AccelerationAction(0)] * 6 + [LaneChangeAction.Right],
      # [AccelerationAction(-10)] + [AccelerationAction(0)] * 8 + [LaneChangeAction.Right],
      # [AccelerationAction(-5)] * 3 + [AccelerationAction(0)] * 10 + [LaneChangeAction.Right],
      # [AccelerationAction(-5)] * 3 + [AccelerationAction(0)] * 12 + [LaneChangeAction.Right],
      # Provoke rear end collision
      # [AccelerationAction(-10)] * 3 + [AccelerationAction(0)] * 2 + [AccelerationAction(5)] * 3 + [
      #   LaneChangeAction.Right] + [AccelerationAction(5)] * 20,
    ]
    visualize_traces(traces_to_visualize)
