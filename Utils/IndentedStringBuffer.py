import os
from typing import Iterable, List, Tuple

class IndentedStringBuffer:
  def __init__(self, src=None, indent : str ="  "):
    self.lines : List[Tuple[int, str]]= []
    self.indent_string : str = indent
    self.current_indent : int = 0
    if src is not None:
      self.add(src)

  def add(self, other="", split_lines=True):
    if isinstance(other, str):
      if split_lines:
        self.lines.extend((self.current_indent, line) for line in other.split(os.linesep))
      else:
        self.lines.append((self.current_indent, other))
    elif isinstance(other, IndentedStringBuffer):
      if split_lines:
        self.lines.extend((self.current_indent + indent, line) for indent, line in other.lines)
      else:
        self.lines.append((self.current_indent, str(other)))
    elif isinstance(other, Iterable):
      for x in other:
        self.add(x)
    else:
      raise TypeError(f"wrong argument type in {__name__}. Expected str, {self.__class__.__name__} or iterables thereof. Got {other.__class__.__name__}")

  def add_to_current_line(self, other : str):
    indent, line = self.lines[-1]
    self.lines[-1] = (indent, line+other)

  def indent(self):
    self.current_indent += 1

  def unindent(self):
    if self.current_indent == 0:
      raise RuntimeError("tried to decrease indentation below 0")
    self.current_indent -= 1

  def __str__(self):
    return os.linesep.join(self.indent_string * indent + line for indent, line in self.lines)