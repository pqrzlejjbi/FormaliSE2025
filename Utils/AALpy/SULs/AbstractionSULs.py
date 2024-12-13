import bisect
import itertools
from typing import Callable, Any, TypeVar

from Utils.AALpy.SULs.WrappingSUL import WrappingSUL
from aalpy.base import SUL

class ValueAbstractionSUL(WrappingSUL):
  def __init__(self, sul: SUL, input_abstraction : Callable = None, output_abstraction : Callable = None):
    super().__init__(sul)
    self.sul = sul

    identity = lambda x: x
    self.in_abstraction = input_abstraction or identity
    self.out_abstraction = output_abstraction or identity

  def step(self, letter):
    letter = self.in_abstraction(letter)
    out = self.sul.step(letter)
    return self.out_abstraction(out)

def discretization(args) -> Callable[[float], Any]:
  """
  Returns a discretization function based on the patter given by the arguments.
  The args should be an interleaving of discretization values and thresholds.
  If the value to be discretized is equal to a threshold the lower value is chosen.

  Example:
    discretization("low", 10, "mid", 20, "high")(15) == "mid"
    discretization("low", 10, "mid", 20, "high")(10) == "low"
  """

  if len(args) % 2 != 1:
    raise ValueError("expected odd number of arguments")

  thresholds = [val for idx, val in enumerate(args) if idx % 2 == 1]
  values = [val for idx, val in enumerate(args) if idx % 2 == 0]

  if any(n < c for c, n in itertools.pairwise(thresholds)):
    raise ValueError("thresholds are not sorted")

  def inner(val : float):
    idx = bisect.bisect_left(thresholds, val)
    return values[idx]
  return inner

class TemporalAbstractionSUL(WrappingSUL):
  def __init__(self, sul: SUL, action_dict: dict[str, list], output_abstraction: Callable[[list], Any]):
    super().__init__(sul)
    self.action_dict = action_dict
    self.output_abstraction = output_abstraction

  def step(self, step=None):
    out_sequence = []
    for in_sym in self.action_dict[step]:
      small_step_output = super().step(in_sym)
      out_sequence.append(small_step_output)
    big_step_output = self.output_abstraction(out_sequence)
    return big_step_output