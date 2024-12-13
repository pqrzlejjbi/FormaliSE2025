from typing import Iterable, Callable, TypeVar, Any, MutableMapping

KT = TypeVar("KT")
VT = TypeVar("VT")

class CustomKeyDict(MutableMapping[KT, VT]):
  def __init__(self, key_fun : Callable[[KT], Any] = None, iterable : Iterable[tuple[KT, VT]] = None):
    if key_fun is None:
      key_fun = id
    if iterable is None:
      iterable = []
    self.dict = dict((key_fun(key), (key, val)) for key,val in iterable)
    self.key_function = key_fun

  def __len__(self):
    return len(self.dict)

  def keys(self):
    return (k for k,v in self.dict.values())

  def values(self):
    return (v for k,v in self.dict.values())

  def items(self):
    return self.dict.values()

  def __getitem__(self, item):
    return self.dict[self.key_function(item)][1]

  def __delitem__(self, item):
    del self.dict[self.key_function(item)]

  def __setitem__(self, key, value):
    self.dict[self.key_function(key)] = (key, value)

  def __contains__(self, item):
    return self.key_function(item) in self.dict

  def __iter__(self):
    return self.keys()
