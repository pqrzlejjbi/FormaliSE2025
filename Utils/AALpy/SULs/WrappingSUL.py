from Utils.Decorators import hooked_method, hooked_class
from aalpy.base import SUL

class WrappingSUL(SUL):
  def __init__(self, sul : SUL):
    super().__init__()
    self.sul = sul

  def pre(self):
    self.sul.pre()

  def post(self):
    self.sul.post()

  def step(self, letter):
    return self.sul.step(letter)

  def get_sul(self, condition = None) -> SUL | None:
    """
    Obtain the first wrapped SuL that satisfies a given condition. If no condition is given, returns the innermost SuL.
    Returns None if a condition is given, but no SuL matching it is found.
    """
    sul = self.sul
    while isinstance(sul, WrappingSUL):
      if condition and condition(sul):
        return sul
      sul = sul.sul
    if condition:
      return None
    return sul

@hooked_class
class HookedSUL(WrappingSUL):
  def __init__(self, sul : SUL):
    super().__init__(sul)

  @hooked_method(True, True)
  def step(self, letter):
    return super().step(letter)

  @hooked_method(True, False)
  def pre(self):
    super().pre()

  @hooked_method(True, False)
  def post(self):
    super().post()

class RepetitionSUL(WrappingSUL):
  def __init__(self, sul: SUL, repeats: int):
    super().__init__(sul)
    if repeats < 1:
      raise ValueError("Have to repeat at least once")
    self.repeats = repeats

  def step(self, letter):
    out = None
    for _ in range(self.repeats):
      out = self.sul.step(letter)
    return out

# TODO should incorporate caching inheriting from (my) CacheSUL using SinkStateCacheTree
class ConditionalSinkStateSUL(WrappingSUL):
  def __init__(self, sul, sink_states = None):
    super().__init__(sul)
    self.sink_states = set(sink_states) or set()

    self.current_sink = None

  def pre(self):
    super().pre()
    self.current_sink = None

  def check_sink(self, letter):
    """Used to report a sink state. Truthy values are interpreted as sinks."""
    pass

  def step(self, letter):
    self.current_sink = self.current_sink or self.check_sink(letter)
    if self.current_sink:
      return self.current_sink
    ret = super().step(letter)
    if ret in self.sink_states:
      self.current_sink = ret
    return ret

class TrackingSUL(WrappingSUL):
  def __init__(self, sul: SUL):
    super().__init__(sul)
    self.io_sequences = []
    self.current_sequence = []

  def pre(self):
    super().pre()
    self.current_sequence = []

  def post(self):
    super().post()
    self.io_sequences.append(self.current_sequence)

  def step(self, letter):
    ret = super().step(letter)
    self.current_sequence.append((letter, ret))
    return ret