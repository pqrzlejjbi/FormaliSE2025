from Utils.AALpy.SULs.CacheTree import CacheTree

class SinkStateCacheTree(CacheTree):
  def __init__(self, sink_states : list):
    CacheTree.__init__(self)
    self.sink_states : list = sink_states

  def insert(self, inp, out):
    c_out = self.curr_node.value
    if c_out not in self.sink_states:
      super().insert(inp, out)
    elif c_out != out :
      raise ValueError(f"Violation of sink state assumption: {list(zip(self.inputs, self.outputs))}")

  def lookup(self, inp) :
    c_out = self.curr_node.value
    if c_out in self.sink_states:
      return c_out
    else:
      return super().lookup(inp)

  def step(self, inp):
    if self.curr_node.value not in self.sink_states:
      super().step(inp)