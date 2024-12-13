from Utils.AALpy.SULs.SinkStateCacheTree import SinkStateCacheTree
from Utils.AALpy.SULs.WrappingSUL import WrappingSUL, ConditionalSinkStateSUL
from aalpy.base.SUL import SUL
from Utils.AALpy.SULs.CacheTree import CacheTree

class CacheSUL(WrappingSUL):
  """
  System under learning that keeps a cache of all queries in memory.
  """

  def __init__(self, sul: SUL, cache: CacheTree):
    super().__init__(sul)
    self.cache: CacheTree = cache

    self.cached: bool = True

  def pre(self):
    self.cache.reset()
    self.cached = True

  def step(self, letter):
    """
    Obtains the response to a given action by either
    - obtaining it from the cache
    - performing it on the system under learning

    Args:
       letter: Single input that is executed on the SUL.

    Returns:
       Output received after executing the input.
    """
    if self.cached:
      out = self.cache.lookup_step(letter)
      if out is not self.cache.missing:
        return out
      # action was not cached, have to initiate a real query
      self.cached = False
      self.sul.pre()
      for inp in self.cache.inputs:
        self.sul.step(inp)

    out = self.sul.step(letter)
    self.cache.insert_step(letter, out)
    return out

# TODO could be integrated into CSS SUL.
class CachedSinkStateSUL(CacheSUL):
  def __init__(self, sul: ConditionalSinkStateSUL, cache_tree: SinkStateCacheTree = None, check_sink_alphabet=None):
    self.check_sink_alphabet = check_sink_alphabet or []

    cache_tree = cache_tree or SinkStateCacheTree(sul.sink_states)

    sym_diff = set(cache_tree.sink_states)
    sym_diff.symmetric_difference_update(sul.sink_states)
    if len(sym_diff) != 0:
      raise ValueError(f"Cache and SUL don't agree on sink states: {sym_diff}")

    super().__init__(sul, cache_tree)

  def step(self, in_sym):
    out = super().step(in_sym)
    if not self.cached:
      for in_sym in self.check_sink_alphabet:
        out_sym = self.sul.check_sink(in_sym)
        if out_sym:
          self.cache.insert_step(in_sym, out_sym)
    return out