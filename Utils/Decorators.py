import inspect
from collections import defaultdict
from functools import wraps, partial
from inspect import signature, getfullargspec, Parameter, get_annotations
from typing import Dict, Type, Callable, Any, TypeVar, ParamSpec

import typing

from Utils.GeneralUtils import fallback_if_none

T = TypeVar("T")
P = ParamSpec("P")
P2 = ParamSpec("P2")
Fun = Callable[P, T]
Wrapper = Callable[[Fun], Fun]

def is_positional(param: Parameter):
  return param.kind in [Parameter.POSITIONAL_ONLY, Parameter.POSITIONAL_OR_KEYWORD]

def is_keyword(param: Parameter):
  return param.kind in [Parameter.KEYWORD_ONLY, Parameter.POSITIONAL_OR_KEYWORD]

def is_var(param: Parameter):
  return param.kind in [Parameter.VAR_KEYWORD, Parameter.VAR_POSITIONAL]

def get_default_args(func):
  candidates = inspect.signature(func).parameters.items()
  return {
    name : val.default for name, val in candidates
    if val.default is not inspect.Parameter.empty
  }

class FunctionParameters:
  # TODO thorough testing
  # TODO add methods for validation (required arguments, types)
  def __init__(self, function : Callable, args, kwargs):
    self.fun = function
    sig = signature(function)
    self.signature = sig

    # TODO can we simplify this by discerning only between pos only, var args kw args and var kw args?
    self.args_dict = dict()
    self.kwargs_dict = dict()
    self.var_kwargs = dict()
    self.var_kwargs_name = None
    self.var_args = []
    self.var_args_name = None

    self.set_args(args, kwargs)

  def set_args(self, args : tuple = None, kwargs : dict = None) -> 'FunctionParameters':
    args = fallback_if_none(args, tuple())
    kwargs = fallback_if_none(kwargs, dict())

    spec_args = []
    spec_kwonlyargs = []
    for name, parameter in self.signature.parameters.items():
      if is_positional(parameter):
        spec_args.append(name)
      if parameter.kind == parameter.KEYWORD_ONLY:
        spec_kwonlyargs.append(name)
      if parameter.kind == parameter.VAR_POSITIONAL:
        self.var_args_name = name
      if parameter.kind == parameter.VAR_KEYWORD:
        self.var_kwargs_name = name

    # anything shared between args and spec_args is a positional argument
    min_args = min(len(args), len(spec_args))
    for idx in range(min_args):
      self.args_dict[spec_args[idx]] = args[idx]

    # all positional args that are not in the spec are variadic positional
    self.var_args = list(args[min_args:])
    # all missing positional args have to be provided as keyword args
    kwp_args = spec_args[min_args:]

    # split required and variadic kwargs
    for name, value in kwargs.items():
      if name in kwp_args or name in spec_kwonlyargs:
        self.kwargs_dict[name] = value
      else:
        self.var_kwargs[name] = value

    return self

  def get_set_args(self) -> typing.Iterable[tuple[str, Any]]:
    yield from self.args_dict.items()
    if self.var_args_name is not None:
      yield self.var_args_name, self.var_args
    yield from self.kwargs_dict.items()
    if self.var_kwargs_name is not None:
      yield self.var_kwargs_name, self.var_kwargs

  def get_unset_args(self) -> typing.Iterable[str]:
    return filter(lambda x: x not in self, self.signature.parameters.keys())

  def __getitem__(self, name):
    if name in self.args_dict:
      return self.args_dict[name]
    if name in self.kwargs_dict:
      return self.kwargs_dict[name]
    if name == self.var_kwargs_name:
      return self.var_kwargs
    if name == self.var_args_name:
      return self.var_args
    raise KeyError(f"parameter {name} not present")

  def __setitem__(self, name, value):
    if name in self.args_dict:
      self.args_dict[name] = value
    elif name in self.kwargs_dict:
      self.kwargs_dict[name] = value
    elif name == self.var_kwargs_name:
      self.var_kwargs = value
    elif name == self.var_args_name:
      self.var_args = value
    else:
      if not name in self.signature.parameters:
        raise ValueError(f"Invalid parameter name {name}")
      parameter = self.signature.parameters[name]
      if is_keyword(parameter): # prioritize KWs to avoid 'holes' in positional args
        self.kwargs_dict[name] = value
      else:
        self.args_dict[name] = value

  def set_default_args(self, force=False) -> 'FunctionParameters':
    for name, param in self.signature.parameters.items():
      # Ignore if no default parameter is given. Should include variadic parameters
      if param.default == self.signature.empty:
        continue

      # Overwrite existing parameters if forced
      if force and name in self.args_dict:
        self.args_dict[name] = param.default
      if force and name in self.kwargs_dict:
        self.kwargs_dict[name] = param.default

      # Ignore existing parameters if not forced
      if name in self.args_dict or name in self.kwargs_dict:
        continue

      # Prioritize KW args but order should be irrelevant
      if is_keyword(param):
        self.kwargs_dict[name] = param.default
      else:
        self.args_dict[name] = param.default
    return self

  def __contains__(self, name) -> bool:
    test_set = set(self.args_dict.keys())
    test_set.update(self.kwargs_dict.keys())
    test_set.add(self.var_args_name)
    test_set.add(self.var_kwargs_name)
    return name in test_set

  def is_complete(self):
    for name, param in self.signature.parameters.items():
      if name not in self and param.default == self.signature.empty:
        return False
    return True

  def convert_back(self) -> tuple[list, dict]:
    # create args list
    args = []
    pos_arg_missing = False
    for name, param in self.signature.parameters.items(): # use signature for correct order of pos
      if name in self.kwargs_dict or not is_positional(param):
        break # reached variadic / KWs -> done

      # detect 'holes' in positional args
      if name not in self.args_dict:
        pos_arg_missing = True
        continue
      if pos_arg_missing and name in self.args_dict:
        raise ValueError("Detected hole in positional args")

      args.append(self.args_dict[name])
    args.extend(self.var_args)

    kwargs = dict(**self.kwargs_dict, **self.var_kwargs)
    return args, kwargs

  def to_variable_assignment(self, allow_default = True, require_complete = True) -> dict[str, Any]:
    ret = dict()
    for name, param in self.signature.parameters.items():
      if name == self.var_args_name:
        ret[name] = self.var_args
      elif name == self.var_kwargs_name:
        ret[name] = self.var_kwargs
      elif name in self.args_dict:
        ret[name] = self.args_dict[name]
      elif name in self.kwargs_dict:
        ret[name] = self.kwargs_dict[name]
      elif allow_default and param.default != self.signature.empty:
        ret[name] = param.default
      elif require_complete:
        raise ValueError(f"Parameter {name} not present in function {self.fun.__name__}")
    return ret

  def apply(self):
    args, kwargs = self.convert_back()
    return self.fun(*args, **kwargs)

def wraps_with_default_args(wrapped : Callable[P,T]):
  """
  Decorator for wrapping functions with default arguments
  :param wrapped: the function that the decorated function wraps
  :return:
  """

  default_args = get_default_args(wrapped)
  spec = getfullargspec(wrapped)

  def decorator(wrapper : Callable[P2,T]) -> Callable[P,T]:
    @wraps(wrapped)
    def inner(*args, **kwargs):
      new_kwargs = dict(default_args)
      # remove default arguments given by args
      for idx in range(min(len(args), len(spec.args))):
        name = spec.args[idx]
        if name in new_kwargs:
          del new_kwargs[name]
      new_kwargs.update(kwargs)
      return wrapper(*args, **new_kwargs)
    return inner

  return decorator

def wrap_hinted_types(transformations : Dict[Type, Callable[[Any],Any]], transform_default_args = False) -> Wrapper:
  """
  Transforms all inputs that have specific type hints using a given transformation.
  Note that this results in misleading annotations if a transformations input and output types don't match.

  :param transformations: Dict mapping types to transformations
  :param transform_default_args: Whether default arguments should also be transformed
  :return:
  """
  if transform_default_args:
    # TODO Transform default args in a preprocessing step (should be done in `decorator`)
    raise NotImplementedError("Transformation of default args not implemented")

  identity = lambda x : x
  transformations = defaultdict(lambda : identity, transformations)

  def decorator(f):
    params = signature(f).parameters
    spec = getfullargspec(f)
    annos = defaultdict(lambda : None, get_annotations(f))
    def transform(name : str, arg : Any) -> Any:
      return transformations[annos[name]](arg)

    var_arg_name = spec.varargs
    var_kw_arg_name = spec.varkw

    @wraps(f)
    def inner(*args, **kwargs):
      used_args = set()
      for arg_name in kwargs.keys():
        is_single_kw_arg = arg_name in params.keys() and is_keyword(params[arg_name])
        key_pick = arg_name if is_single_kw_arg else var_kw_arg_name
        kwargs[arg_name] = transform(key_pick, kwargs[arg_name])
        if is_single_kw_arg and params[arg_name].kind == Parameter.POSITIONAL_OR_KEYWORD:
          used_args.add(arg_name)

      remaining_params = [name for name, param in params.items() if is_positional(param) and name not in used_args]
      new_args = [None] * len(args)
      for idx in range(len(args)):
        key_pick = remaining_params[idx] if idx < len(remaining_params) else var_arg_name
        new_args[idx] = transform(key_pick, args[idx])

      return f(*new_args, **kwargs)
    return inner
  return decorator

class Hooked(Callable[P, T]):
  class CallbackHandle:
    def __init__(self, fun):
      self._fun = fun

    def unregister(self):
      self._fun(self)

  def __init__(self, fun: Callable[P, T], feed_args, feed_ret):
    self.feed_args_default = feed_args
    self.feed_ret_default = feed_ret

    self.pre = dict()
    self.post = dict()

    self.fun = fun

  def register_pre(self, fun, feed_args = None):
    feed_args = self.feed_args_default if feed_args is None else feed_args
    key = Hooked.CallbackHandle(self.un_register_pre)
    self.pre[key] = (fun, feed_args)
    return key

  def un_register_pre(self, key):
    del self.pre[key]

  def register_post(self, fun, feed_args = None, feed_ret = None):
    feed_args = self.feed_args_default if feed_args is None else feed_args
    feed_ret = self.feed_ret_default if feed_ret is None else feed_ret
    key = Hooked.CallbackHandle(self.un_register_post)
    self.post[key] = (fun, feed_args, feed_ret)
    return key

  def un_register_post(self, key):
    del self.post[key]

  def __call__(self, *args : P.args, **kwargs : P.kwargs) -> T:
    full_args = (args, kwargs)
    no_args = ([], dict())

    for pre, feed_args in self.pre.values():
      if feed_args:
        args_2, kwargs_2 = full_args
      else:
        args_2, kwargs_2 = no_args
      pre(*args_2, **kwargs_2)

    ret = self.fun(*args, **kwargs)

    for post, feed_args, feed_ret in self.post.values():
      if feed_args:
        args_2, kwargs_2 = full_args
      else:
        args_2, kwargs_2 = no_args
      if feed_ret:
        args_2 = (ret, *args_2)
      post(*args_2, **kwargs_2)

    return ret


hook_marker = "_hook_marker_"

def hooked_class(cls: Type[T]) -> Type[T]:
  # obtain original init and methods
  orig_init = cls.__init__
  hooked_methods = {key : val for key, val in cls.__dict__.items() if hasattr(val, hook_marker)}

  # monkey patch init to create methods with per instance hooks
  def init(self, *args, **kwargs):
    for name, fun in hooked_methods.items():
      hook_args = getattr(fun, hook_marker)
      setattr(self, name, Hooked(partial(fun, self), *hook_args))
    orig_init(self, *args, **kwargs)
  cls.__init__ = init

  # monkey patch hooked methods in the class object
  def call(name, self, *args, **kwargs):
    return getattr(self, name)(*args, **kwargs)
  for name in hooked_methods.keys():
    setattr(cls, name, partial(call, name))

  # return class
  return cls

#TODO get type hinting right
def hooked_method(feed_args = False, feed_ret = False):
  def decorator(fun : Callable[P, T]) -> Hooked[P, T]:
    setattr(fun, hook_marker, (feed_args, feed_ret))
    return fun # This is okay. See `hooked_class`
  return decorator

def hooked_function(feed_args = False, feed_ret = False):
  def decorator(fun : Callable[P, T]) -> Hooked[P, T]:
    return Hooked(fun, feed_args, feed_ret)
  return decorator
