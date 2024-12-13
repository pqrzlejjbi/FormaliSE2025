from collections.abc import Mapping
from typing import TypeVar

KT = TypeVar("KT")
VT = TypeVar("VT")

class CompositeMapping(Mapping[KT, VT]):
  """Gives a view into a list of Mappings"""
  def __len__(self):
    return sum(len(part) for part in self.parts)

  def __init__(self, parts : list[Mapping]):
    self.parts = parts

  def __contains__(self, item):
    return any(item in part for part in self.parts)

  def __getitem__(self, item):
    missing = object()
    for part in self.parts:
      ret = part.get(item, missing)
      if not ret is missing:
        return ret
    raise KeyError(f"Missing key {item} in CompositeMapping")

  def __iter__(self):
    for part in self.parts:
      yield from part