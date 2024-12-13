import itertools
from pathlib import Path
from typing import Iterable
from xsdata.formats.dataclass.parsers import XmlParser
from aalpy.base import SUL

from Utils.OpenScenario.SimulationUtils import get_vehicle_name_by_idx, get_object_state, Local_KPI_Function, \
  Reduce_KPI_Function, StopCondition, ObjectState
import lib.esminiLib as esmini
import lib.esminiRMLib as RM
from lib.xosc import OpenScenario
from Utils.CtypesUtils import cast_to_ptr, make_string_array


def getXOSC(file : str | Path) -> OpenScenario:
  return XmlParser().from_path(Path(file), OpenScenario)

class SimulationSUL(SUL) :
  # Warning: this class is not threadsafe
  def __init__(
      self, osc_filename, time_step: float = 0, visualize=False, cmd_args="",
      log_to_console = False, log_path = "/dev/null",
      termination_output="terminated"
  ):
    super().__init__()
    self.time_step = time_step

    esmini.SE_LogToConsole(log_to_console)
    if log_path is not None:
      esmini.SE_SetLogFilePath(log_path)

    # create arguments for esmini
    args = ["esmini(lib)", "--osc", osc_filename]
    args += cmd_args.split(" ")
    #se.SE_InitWithArgs(len(args), ctypes.cast(make_string_array(args),ctypes.POINTER(ctypes.POINTER(ctypes.c_char))))
    self.args = args
    self.visualize = None
    self.set_visualize(visualize)

    self.termination_output = termination_output
    self.terminated = False

    # initialize road manager
    odr_relative_path = getXOSC(osc_filename).road_network.logic_file.filepath
    odr_path = Path(osc_filename).parent / odr_relative_path
    RM.RM_SetLogFilePath("/dev/null")
    RM.RM_Init(str(odr_path.resolve()))

    esmini.SE_Init(osc_filename, 0, 0, 0, 0)
    self.object_name_map = {get_vehicle_name_by_idx(idx) : idx for idx in range(esmini.SE_GetNumberOfObjects())}

  def set_visualize(self, visualize):
    windowed_args = ["--window", "0", "0", "900", "500"]
    headless_args = ["--headless"]
    if self.visualize is True:
      self.args = self.args[:-len(windowed_args)]
    if self.visualize is False: # use `is` here to account for None
      self.args = self.args[:-len(headless_args)]

    self.visualize = visualize
    args = windowed_args if visualize else headless_args
    self.args.extend(args)

  def get_object_dict(self) -> dict[str, ObjectState]:
    return {name: get_object_state(idx) for name, idx in self.object_name_map.items()}

  def get_object_list(self) -> list[ObjectState]:
    return [get_object_state(idx) for name, idx in self.object_name_map.items()]

  def reset(self):
    esmini.SE_InitWithArgs(len(self.args), cast_to_ptr(make_string_array(self.args)))
    self.terminated = False

  def pre(self):
    self.reset()

  def post(self):
    esmini.SE_Close()

  def step(self, letter=None):
    if esmini.SE_GetQuitFlag():
      self.terminated = True # TODO maybe this should go after the termination check
    if self.terminated:
      return self.termination_output
    if letter is not None:
      raise NotImplementedError()
    return self.sim_step()

  def sim_step(self):
    if self.time_step == 0:
      prev = esmini.SE_GetSimulationTime()
      esmini.SE_Step()
      return esmini.SE_GetSimulationTime() - prev
    else:
      esmini.SE_StepDT(self.time_step)
      return self.time_step

  def run_sim(self, *, inputs : Iterable = None,
      kpi_reduce_fun : Reduce_KPI_Function = None,
      kpi_fun : Local_KPI_Function = None,
      abort_cond : StopCondition = None,
    ):
    if abort_cond is None:
      abort_cond = lambda x: False
    if inputs is None:
      inputs = itertools.repeat(None)

    kpis = []
    self.pre()
    object_dict = self.get_object_dict()
    for letter in inputs:
      if esmini.SE_GetQuitFlag() == 1 or abort_cond(object_dict):
        break

      ret = self.step(letter)
      object_dict = self.get_object_dict()
      if kpi_fun:
        ret = kpi_fun(object_dict)
      kpis.append(ret)

    self.post()
    return kpis if kpi_reduce_fun is None else kpi_reduce_fun(kpis)