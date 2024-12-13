import itertools
import math
from typing import Callable, Any

import more_itertools
import numpy as np

class Slice:
  def __getitem__(self, item):
    return item
Slice = Slice()

def fallback_if_none(value, fallback):
  return value if value is not None else fallback

def filter_dict(function : Callable[[Any, Any], bool], dictionary : dict, in_place = False):
  if in_place:
    negative = filter(lambda x: not function(*x), dictionary.items())
    for key, _ in list(negative):
      del dictionary[key]
    return dictionary
  else:
    return dict(filter(lambda x: function(*x), dictionary.items()))

def count_from_to(start=0, to=None, step=1, allow_inexact_last=True):
  if to is None:
    yield from itertools.count(start, step)
  else:
    yield from more_itertools.numeric_range(start, to, step)
    remainder = math.remainder((to - start), step)
    exact_cond = remainder == 0
    inexact_cond = allow_inexact_last and np.isclose(remainder, 0) and remainder < 0
    if exact_cond or inexact_cond :
      yield to

class SimpleEnumMeta(type):
  # TODO can we improve typing support for this?

  def __len__(self):
    return sum(1 for _ in self)

  def __iter__(self):
    for k, v in self.__dict__.items():
      if k.startswith("__") or isinstance(v, (classmethod, staticmethod)):
        continue
      yield v

  def __contains__(self, item):
    return item in list(self)

class SimpleEnum(metaclass=SimpleEnumMeta):
  """Alternative enumeration without instance values. Basically a collection of literals with minimal typing support"""
  def __init__(self):
    # this could be moved to the metaclass e.g. by overriding self.__new__ in __init__ or __new__?
    raise RuntimeError("This class should never be instantiated")