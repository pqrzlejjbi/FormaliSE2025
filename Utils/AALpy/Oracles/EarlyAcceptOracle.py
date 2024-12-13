from typing import Callable

from aalpy import Oracle, Automaton

class EarlyAcceptOracle(Oracle):
  def __init__(self, accept_condition : Callable[[Automaton], bool], other_oracle : Oracle, callback: Callable = None):
    super().__init__(other_oracle.alphabet, other_oracle.sul)
    self.accept_cond = accept_condition
    self.other_oracle = other_oracle
    self.callback = callback if callback else lambda: None

  def find_cex(self, hypothesis):
    self.callback()
    if self.accept_cond(hypothesis):
      return None
    ret = self.other_oracle.find_cex(hypothesis)
    self.num_queries = self.other_oracle.num_queries
    self.num_steps = self.other_oracle.num_steps
    self.callback()
    return ret

  def reset_hyp_and_sul(self, hypothesis):
    raise NotImplementedError("This method should never be called.")