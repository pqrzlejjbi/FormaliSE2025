import builtins
import datetime
import hashlib
import inspect
import os
import pickle
import queue
from collections.abc import MutableMapping
from functools import wraps
from inspect import signature
from typing import Callable, TypeVar, Generic, ParamSpec
from pathlib import Path

from Utils.Decorators import wraps_with_default_args, FunctionParameters, Wrapper

class OutputDataManagement:
  _default = None
  @classmethod
  def get_default(cls, *args, **kwargs):
    if cls._default is None or len(args) != 0 or len(kwargs) != 0:
      cls._default = cls(*args, **kwargs)
    return cls._default

  def __init__(self, out_path ="output", per_run_folders = True):
    self._out_path = Path(out_path).resolve()
    self._per_run_folders = per_run_folders
    self._base_wd = Path.cwd()
    self._out_path.mkdir(parents=True, exist_ok=True)
    self._dirty = False

    self._run_path = None

    if not self._per_run_folders:
      self._run_path = self._out_path
    else:
      self.new_run()


  def make_dirty(self):
    if self._dirty:
      return

    subfolders = {file.name for file in self._out_path.iterdir() if file.is_dir()}
    idx = 0
    date_str = datetime.date.today().strftime("%Y_%m_%d")
    while True:
      run_folder = f"{date_str}_run_{idx}"
      if run_folder not in subfolders:
        break
      idx += 1
    self._run_path = self._out_path / run_folder
    os.mkdir(self._run_path)

    if not os.path.isdir(self._run_path):
      raise EnvironmentError("Run folder is not a folder")

    self._dirty = True

  @staticmethod
  def set_self_and_use(use=True):
    def decorator(f):
      @wraps(f)
      def inner(self=None, *args, **kwargs):
        if self is None:
          self = OutputDataManagement.get_default()
        if use:
          self.make_dirty()
        return f(self, *args, **kwargs)
      return inner
    return decorator

  @set_self_and_use(False)
  def new_run(self):
    self._dirty = False

  @set_self_and_use()
  def get_path(self=None, *, path = ""):
    return self._run_path / path

  @set_self_and_use()
  def open(self=None, *, path = "name", mode = "w"):
    return open(self.get_path(path), mode)

def dump(path: Path | str, data):
  path = Path(path)
  try:
    with open(path, "wb") as file:
      pickle.dump(data, file)
  except:
    if path.is_file():
      path.unlink(missing_ok=True)
    raise

def load(path: Path | str):
  with open(path, "rb") as file:
    return pickle.load(file)

T = TypeVar("T")
P = ParamSpec("P")

class PickledValue(Generic[T]):
  def __init__(self, filename : str, ctor : Callable[[], T], methods_to_track = None, autosave_interval = None):
    self.filename = Path(filename)
    self.filename.parent.mkdir(parents=True,exist_ok=True)
    self.value : T

    try:
      self.value = load(self.filename)
    except:
      self.value = ctor()

    self.dirty = False
    self.tracked_method_map = dict()
    self.track_methods = methods_to_track is not None

    self.autosave = autosave_interval is not None
    self.steps_until_autosave = autosave_interval
    self.autosave_interval = autosave_interval

    if methods_to_track is not None:
      if methods_to_track == "all":
        methods_to_track = [k for k, _ in inspect.getmembers(self.value, inspect.ismethod)]
      for fn_to_track in methods_to_track:
        real_fun = getattr(self.value, fn_to_track)
        def fake_fun(*args, **kwargs):
          self.dirty = True
          value = real_fun(*args, **kwargs)
          if self.autosave:
            self.steps_until_autosave -= 1
            if self.steps_until_autosave == 0:
              self.save()
              self.steps_until_autosave = self.autosave_interval
          return value
        self.tracked_method_map[fn_to_track] = (real_fun, fake_fun)
      self.set_fake_funs()

  def set_fake_funs(self):
    self.set_funs(1)

  def set_real_funs(self):
    self.set_funs(0)

  def set_funs(self, idx):
    for name, funs in self.tracked_method_map.items():
      setattr(self.value, name, funs[idx])

  def save(self, force = False):
    if not self.track_methods:
      dump(self.filename, self.value)
    elif self.dirty or force:
      self.set_real_funs()
      dump(self.filename, self.value)
      self.set_fake_funs()
    self.dirty = False

class PickledDict(MutableMapping):
  def __init__(self, folder, transform = None):
    self.folder = Path(folder)
    self.folder.mkdir(parents=True, exist_ok=True)

    self.key_transform_ = transform or (lambda x : str(x))

  def key_transform(self, key):
    key = self.key_transform_(key)
    if "/" in key:
      raise RuntimeError("The key transform might point outside the folder containing the pickles")
    return self.folder / key

  def __setitem__(self, __key, __value):
    dump(self.key_transform(__key), __value)

  def __delitem__(self, __key):
    path = self.key_transform(__key)
    path.unlink(missing_ok=True)

  def __getitem__(self, __key):
    return load(self.key_transform(__key))

  def keys(self):
    return os.listdir(self.folder)

  def __len__(self):
    return len(self.keys())

  def __iter__(self):
    yield from self.keys()

  def __contains__(self, item):
    return self.key_transform(item).name in self.keys()

  def get_or_compute(self, key, compute):
    if key not in self:
      ret = compute()
      self[key] = ret
      return ret
    return self[key]

def hash(obj):
  binary = pickle.dumps(obj)
  return hashlib.sha256(binary).hexdigest()

def compute_or_unpickle(path: Path, function: Callable, args, kwargs, ignored_args: list[str] = None, verbose: bool = False):
  """
  obtains data either by:
  - computing it from a function with parameters
  - loading it from a pickle
  in the former case, the result is stored in a pickle named after the hash of the arguments
  if a file corresponding to the hash of the arguments already exists, the result is retrieved from there

  parameters:
    file_name : folder containing the pickles
    function : function for determining the operation
    args / kwargs : arguments for the function

  returns:
    function(*args, **kwargs)
  """

  # hash parameters
  parameters = FunctionParameters(function, args, kwargs).to_variable_assignment()
  if ignored_args:
    for ign in ignored_args:
      del parameters[ign]
  binary_params = pickle.dumps(parameters)
  param_hash = hashlib.sha256(binary_params).hexdigest()

  # create folders
  path = Path(path)
  path.mkdir(parents=True, exist_ok=True)
  path = path / param_hash

  # TODO add safe version that also checks equality of arguments if hashes match
  if path.exists():
    if verbose:
      print("loading from file:", path.parent.name)
    result = load(path)
  else:
    if verbose:
      print("recomputing:", path.parent.name)
    result = function(*args, **kwargs)
    dump(path, result)
  return result

class PickleCache:
  # TODO maybe encapsulate default values in a base class or a decorator
  _default = None
  @classmethod
  def get_default(cls, *args, **kwargs):
    if cls._default is None or len(args) != 0 or len(kwargs) != 0:
      cls._default = cls(*args, **kwargs)
    return cls._default

  def __init__(self, base_path=".", verbose=False):
    self.base_path = Path(base_path)
    self.verbose = verbose

  def __call__(self, name=None, ignored_args=None) -> Wrapper:
    def decorator(f):
      folder = name or f.__name__

      def fun(*args, **kwargs):
        return compute_or_unpickle(self.base_path / folder, f,  args, kwargs, ignored_args, self.verbose)
      return fun
    return decorator

  def add_folder(self, folder_name):
    self.base_path = self.base_path / folder_name

class LazyPickle(Generic[T]):
  hash_path = "hash"
  data_path = "data"

  def __init__(self, func: Callable, args: tuple, kwargs: dict, base_path: Path):
    self.func = func
    self.args = args
    self.kwargs = kwargs
    self.base_path = base_path

    self.is_eval = False
    self.value = None
    self.hash = None

  def get_hash(self):
    if not isinstance(self, LazyPickle):
      return hash(self)
    self.compute_or_load(True)
    return self.hash

  def get_value(self) -> T:
    if not isinstance(self, LazyPickle):
      return self
    self.compute_or_load(False)
    return self.value

  def compute_or_load(self, hash_only):
    if self.is_eval or (hash_only and self.hash is not None):
      return

    funpar = FunctionParameters(self.func, self.args, self.kwargs)
    canonical_parameters = funpar.to_variable_assignment()

    hash_dict = dict()
    for name, param in canonical_parameters.items():
      if name == funpar.var_args_name:
        hash_dict[name] = tuple(LazyPickle.get_hash(val) for val in param)
      elif name == funpar.var_kwargs_name:
        hash_dict[name] = {key: LazyPickle.get_hash(val) for key, val in param.items()}
      else:
        hash_dict[name] = LazyPickle.get_hash(param)
    param_hash = hash(hash_dict)

    path = self.base_path / param_hash
    if path.exists():
      self.hash = load(path / self.hash_path)
      if not hash_only:
        self.value = load(path / self.data_path)
        self.is_eval = True
    else:
      args = [LazyPickle.get_value(arg) for arg in self.args]
      kwargs = {key: LazyPickle.get_value(val) for key, val in self.kwargs.items()}
      self.value = self.func(*args, **kwargs)
      self.hash = hash(self.value)
      self.is_eval = True

      try:
        path.mkdir(parents=True, exist_ok=True)
        dump(path / self.hash_path, self.hash)
        dump(path / self.data_path, self.value)
      except Exception as e:
        (path / self.hash_path).unlink(True)
        (path / self.data_path).unlink(True)
        path.rmdir()
        raise e
