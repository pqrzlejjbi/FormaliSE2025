from typing import Callable

from Utils.OpenScenario.KPIs import StatefulKPI
from Utils.OpenScenario.Simulation.SimulationSUL import SimulationSUL
from Utils.AALpy.SULs.AbstractionSULs import TemporalAbstractionSUL
from Utils.AALpy.SULs.WrappingSUL import HookedSUL, WrappingSUL
from aalpy.base import SUL


class SmallStepBigStepSUL(WrappingSUL):
  def __init__(self, sul : SimulationSUL, action_dict, output_abstraction, kpis : list[StatefulKPI], prefix_action = None, big_step_wrapper : Callable[[SUL], SUL] = None):
    self.original_sul = sul
    self.kpis = kpis

    # Creation of small step SUL
    def compute_kpis(out_sym, in_sym):
      for kpi in kpis:
        kpi(out_sym)

    self.small_step_sul = HookedSUL(sul)
    self.small_step_sul.step.register_post(compute_kpis)

    # Abstraction
    sul = TemporalAbstractionSUL(self.small_step_sul, action_dict, output_abstraction)

    if big_step_wrapper:
      sul = big_step_wrapper(sul)

    # Creation of big step SUL
    def reset_kpis():
      for kpi in self.kpis:
        kpi.reset()

    def run_prefix():
      if prefix_action in action_dict:
        self.big_step_sul.step(prefix_action)

    self.big_step_sul = HookedSUL(sul)
    self.big_step_sul.pre.register_pre(reset_kpis)
    self.big_step_sul.pre.register_post(run_prefix)

    super().__init__(self.big_step_sul)