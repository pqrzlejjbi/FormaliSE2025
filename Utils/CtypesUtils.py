import ctypes

from ctypes import c_char_p, POINTER, cast

def string_to_char_pointer(string):
  return c_char_p(string.encode("ascii"))

def list_to_array(base_type, values) :
  return (base_type * len(values))(*values)

def make_string_array(strings):
  return list_to_array(c_char_p, [value.encode("ascii") for value in strings])

def cast_to_ptr(obj):
  current_t = obj
  next_t = obj._type_
  depth = 0

  while not isinstance(next_t, str):
    depth += 1
    current_t = next_t
    next_t = next_t._type_

  if next_t == ctypes.c_char_p._type_:
    current_t = ctypes.c_char
    depth += 1
  if next_t == ctypes.c_wchar_p._type_:
    current_t = ctypes.c_wchar
    depth += 1

  if depth == 0:
    return obj

  for _ in range(depth):
    current_t = POINTER(current_t)

  return cast(obj,current_t)
