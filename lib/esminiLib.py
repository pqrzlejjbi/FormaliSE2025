r"""Wrapper for esminiLib.hpp

Generated with:
/usr/local/bin/ctypesgen --include-stdbool -L ./ --library=esminiLib ./esminiLib.hpp -o ./esminiLib.py

Do not modify this file.
"""
from __future__ import annotations

__docformat__ = "restructuredtext"

from dataclasses import dataclass
# Begin preamble for Python

from typing import TypeVar, Type, get_type_hints
import ctypes
import sys
from ctypes import *  # noqa: F401, F403

T = TypeVar("T")

def struct_decorator(cls: Type[T]) -> Type[T]:
    return cls
    # @dataclass(slots=True)
    # class Internal(cls.__base__):
    #     __annotations__ = cls.__annotations__
    #     #__slots__ = list(cls.__annotations__.keys())
    # return Internal

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):
    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = ['./']

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs(['./'])

# Begin libraries
_libs["esminiLib"] = load_library("esminiLib")

# 1 libraries
# End libraries

# No modules

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 52
@struct_decorator
class struct_anon_1(Structure):
    id : c_int
    model_id : c_int
    ctrl_type : c_int
    timestamp : c_float
    x : c_float
    y : c_float
    z : c_float
    h : c_float
    p : c_float
    r : c_float
    roadId : c_int
    junctionId : c_int
    t : c_float
    laneId : c_int
    laneOffset : c_float
    s : c_float
    speed : c_float
    centerOffsetX : c_float
    centerOffsetY : c_float
    centerOffsetZ : c_float
    width : c_float
    length : c_float
    height : c_float
    objectType : c_int
    objectCategory : c_int
    wheel_angle : c_float
    wheel_rot : c_float

struct_anon_1._fields_ = [
    ('id', c_int),
    ('model_id', c_int),
    ('ctrl_type', c_int),
    ('timestamp', c_float),
    ('x', c_float),
    ('y', c_float),
    ('z', c_float),
    ('h', c_float),
    ('p', c_float),
    ('r', c_float),
    ('roadId', c_int),
    ('junctionId', c_int),
    ('t', c_float),
    ('laneId', c_int),
    ('laneOffset', c_float),
    ('s', c_float),
    ('speed', c_float),
    ('centerOffsetX', c_float),
    ('centerOffsetY', c_float),
    ('centerOffsetZ', c_float),
    ('width', c_float),
    ('length', c_float),
    ('height', c_float),
    ('objectType', c_int),
    ('objectCategory', c_int),
    ('wheel_angle', c_float),
    ('wheel_rot', c_float),
]

SE_ScenarioObjectState = struct_anon_1# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 52

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 76
@struct_decorator
class struct_anon_2(Structure):
    global_pos_x : c_float
    global_pos_y : c_float
    global_pos_z : c_float
    local_pos_x : c_float
    local_pos_y : c_float
    local_pos_z : c_float
    angle : c_float
    road_heading : c_float
    road_pitch : c_float
    road_roll : c_float
    trail_heading : c_float
    curvature : c_float
    speed_limit : c_float
    roadId : c_int
    junctionId : c_int
    laneId : c_int
    laneOffset : c_float
    s : c_float
    t : c_float

struct_anon_2._fields_ = [
    ('global_pos_x', c_float),
    ('global_pos_y', c_float),
    ('global_pos_z', c_float),
    ('local_pos_x', c_float),
    ('local_pos_y', c_float),
    ('local_pos_z', c_float),
    ('angle', c_float),
    ('road_heading', c_float),
    ('road_pitch', c_float),
    ('road_roll', c_float),
    ('trail_heading', c_float),
    ('curvature', c_float),
    ('speed_limit', c_float),
    ('roadId', c_int),
    ('junctionId', c_int),
    ('laneId', c_int),
    ('laneOffset', c_float),
    ('s', c_float),
    ('t', c_float),
]

SE_RoadInfo = struct_anon_2# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 76

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 91
@struct_decorator
class struct_anon_3(Structure):
    x : c_float
    y : c_float
    z : c_float
    roadId : c_int
    junctionId : c_int
    laneId : c_int
    osiLaneId : c_int
    laneOffset : c_float
    s : c_float
    t : c_float

struct_anon_3._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('z', c_float),
    ('roadId', c_int),
    ('junctionId', c_int),
    ('laneId', c_int),
    ('osiLaneId', c_int),
    ('laneOffset', c_float),
    ('s', c_float),
    ('t', c_float),
]

SE_RouteInfo = struct_anon_3# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 91

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 99
@struct_decorator
class struct_anon_4(Structure):
    far_left_lb_id : c_int
    left_lb_id : c_int
    right_lb_id : c_int
    far_right_lb_id : c_int

struct_anon_4._fields_ = [
    ('far_left_lb_id', c_int),
    ('left_lb_id', c_int),
    ('right_lb_id', c_int),
    ('far_right_lb_id', c_int),
]

SE_LaneBoundaryId = struct_anon_4# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 99

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 109
@struct_decorator
class struct_anon_5(Structure):
    ds : c_float
    dt : c_float
    dLaneId : c_int
    dx : c_float
    dy : c_float
    oppositeLanes : c_bool

struct_anon_5._fields_ = [
    ('ds', c_float),
    ('dt', c_float),
    ('dLaneId', c_int),
    ('dx', c_float),
    ('dy', c_float),
    ('oppositeLanes', c_bool),
]

SE_PositionDiff = struct_anon_5# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 109

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 121
@struct_decorator
class struct_anon_6(Structure):
    x : c_float
    y : c_float
    z : c_float
    h : c_float
    p : c_float
    speed : c_float
    wheel_rotation : c_float
    wheel_angle : c_float

struct_anon_6._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('z', c_float),
    ('h', c_float),
    ('p', c_float),
    ('speed', c_float),
    ('wheel_rotation', c_float),
    ('wheel_angle', c_float),
]

SE_SimpleVehicleState = struct_anon_6# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 121

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 127
@struct_decorator
class struct_anon_7(Structure):
    name : String
    value : POINTER(None)

struct_anon_7._fields_ = [
    ('name', String),
    ('value', POINTER(None)),
]

SE_Parameter = struct_anon_7# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 127

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 133
@struct_decorator
class struct_anon_8(Structure):
    name : String
    value : POINTER(None)

struct_anon_8._fields_ = [
    ('name', String),
    ('value', POINTER(None)),
]

SE_Variable = struct_anon_8# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 133

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 143
@struct_decorator
class struct_anon_9(Structure):
    active : c_bool
    type : c_int
    number : c_int
    value_type : c_int

struct_anon_9._fields_ = [
    ('active', c_bool),
    ('type', c_int),
    ('number', c_int),
    ('value_type', c_int),
]

SE_OverrideActionStatusGear = struct_anon_9# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 143

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 152
@struct_decorator
class struct_anon_10(Structure):
    active : c_bool
    type : c_int
    value : c_double
    maxRate : c_double
    value_type : c_int

struct_anon_10._fields_ = [
    ('active', c_bool),
    ('type', c_int),
    ('value', c_double),
    ('maxRate', c_double),
    ('value_type', c_int),
]

SE_OverrideActionStatusBrake = struct_anon_10# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 152

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 159
@struct_decorator
class struct_anon_11(Structure):
    active : c_bool
    value : c_double
    maxRate : c_double

struct_anon_11._fields_ = [
    ('active', c_bool),
    ('value', c_double),
    ('maxRate', c_double),
]

SE_OverrideActionStatusPedals = struct_anon_11# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 159

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 167
@struct_decorator
class struct_anon_12(Structure):
    active : c_bool
    value : c_double
    maxRate : c_double
    maxTorque : c_double

struct_anon_12._fields_ = [
    ('active', c_bool),
    ('value', c_double),
    ('maxRate', c_double),
    ('maxTorque', c_double),
]

SE_OverrideActionStatusSteering = struct_anon_12# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 167

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 177
@struct_decorator
class struct_anon_13(Structure):
    throttle : SE_OverrideActionStatusPedals
    brake : SE_OverrideActionStatusBrake
    clutch : SE_OverrideActionStatusPedals
    parkingBrake : SE_OverrideActionStatusBrake
    steeringWheel : SE_OverrideActionStatusSteering
    gear : SE_OverrideActionStatusGear

struct_anon_13._fields_ = [
    ('throttle', SE_OverrideActionStatusPedals),
    ('brake', SE_OverrideActionStatusBrake),
    ('clutch', SE_OverrideActionStatusPedals),
    ('parkingBrake', SE_OverrideActionStatusBrake),
    ('steeringWheel', SE_OverrideActionStatusSteering),
    ('gear', SE_OverrideActionStatusGear),
]

SE_OverrideActionList = struct_anon_13# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 177

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 195
@struct_decorator
class struct_anon_14(Structure):
    id : c_int
    x : c_float
    y : c_float
    z : c_float
    z_offset : c_float
    h : c_float
    roadId : c_int
    s : c_float
    t : c_float
    name : String
    orientation : c_int
    length : c_float
    height : c_float
    width : c_float

struct_anon_14._fields_ = [
    ('id', c_int),
    ('x', c_float),
    ('y', c_float),
    ('z', c_float),
    ('z_offset', c_float),
    ('h', c_float),
    ('roadId', c_int),
    ('s', c_float),
    ('t', c_float),
    ('name', String),
    ('orientation', c_int),
    ('length', c_float),
    ('height', c_float),
    ('width', c_float),
]

SE_RoadSign = struct_anon_14# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 195

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 201
@struct_decorator
class struct_anon_15(Structure):
    fromLane : c_int
    toLane : c_int

struct_anon_15._fields_ = [
    ('fromLane', c_int),
    ('toLane', c_int),
]

SE_RoadObjValidity = struct_anon_15# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 201

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 210
@struct_decorator
class struct_anon_16(Structure):
    width : c_int
    height : c_int
    pixelSize : c_int
    pixelFormat : c_int
    data : POINTER(c_ubyte)

struct_anon_16._fields_ = [
    ('width', c_int),
    ('height', c_int),
    ('pixelSize', c_int),
    ('pixelFormat', c_int),
    ('data', POINTER(c_ubyte)),
]

SE_Image = struct_anon_16# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 210

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 226
if _libs["esminiLib"].has("SE_AddPath", "cdecl"):
    SE_AddPath = _libs["esminiLib"].get("SE_AddPath", "cdecl")
    SE_AddPath.argtypes = [String]
    SE_AddPath.restype = c_int

    ctypes_SE_AddPath = SE_AddPath
    def SE_AddPath(path : String) -> c_int : 
        return ctypes_SE_AddPath(path)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 232
if _libs["esminiLib"].has("SE_ClearPaths", "cdecl"):
    SE_ClearPaths = _libs["esminiLib"].get("SE_ClearPaths", "cdecl")
    SE_ClearPaths.argtypes = []
    SE_ClearPaths.restype = None

    ctypes_SE_ClearPaths = SE_ClearPaths
    def SE_ClearPaths() -> None : 
        return ctypes_SE_ClearPaths()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 249
if _libs["esminiLib"].has("SE_SetLogFilePath", "cdecl"):
    SE_SetLogFilePath = _libs["esminiLib"].get("SE_SetLogFilePath", "cdecl")
    SE_SetLogFilePath.argtypes = [String]
    SE_SetLogFilePath.restype = None

    ctypes_SE_SetLogFilePath = SE_SetLogFilePath
    def SE_SetLogFilePath(logFilePath : String) -> None : 
        return ctypes_SE_SetLogFilePath(logFilePath)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 266
if _libs["esminiLib"].has("SE_SetDatFilePath", "cdecl"):
    SE_SetDatFilePath = _libs["esminiLib"].get("SE_SetDatFilePath", "cdecl")
    SE_SetDatFilePath.argtypes = [String]
    SE_SetDatFilePath.restype = None

    ctypes_SE_SetDatFilePath = SE_SetDatFilePath
    def SE_SetDatFilePath(datFilePath : String) -> None : 
        return ctypes_SE_SetDatFilePath(datFilePath)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 274
if _libs["esminiLib"].has("SE_GetSeed", "cdecl"):
    SE_GetSeed = _libs["esminiLib"].get("SE_GetSeed", "cdecl")
    SE_GetSeed.argtypes = []
    SE_GetSeed.restype = c_uint

    ctypes_SE_GetSeed = SE_GetSeed
    def SE_GetSeed() -> c_uint : 
        return ctypes_SE_GetSeed()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 283
if _libs["esminiLib"].has("SE_SetSeed", "cdecl"):
    SE_SetSeed = _libs["esminiLib"].get("SE_SetSeed", "cdecl")
    SE_SetSeed.argtypes = [c_uint]
    SE_SetSeed.restype = None

    ctypes_SE_SetSeed = SE_SetSeed
    def SE_SetSeed(seed : c_uint) -> None : 
        return ctypes_SE_SetSeed(seed)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 292
if _libs["esminiLib"].has("SE_SetWindowPosAndSize", "cdecl"):
    SE_SetWindowPosAndSize = _libs["esminiLib"].get("SE_SetWindowPosAndSize", "cdecl")
    SE_SetWindowPosAndSize.argtypes = [c_int, c_int, c_int, c_int]
    SE_SetWindowPosAndSize.restype = None

    ctypes_SE_SetWindowPosAndSize = SE_SetWindowPosAndSize
    def SE_SetWindowPosAndSize(x : c_int, y : c_int, w : c_int, h : c_int) -> None : 
        return ctypes_SE_SetWindowPosAndSize(x, y, w, h)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 304
if _libs["esminiLib"].has("SE_RegisterParameterDeclarationCallback", "cdecl"):
    SE_RegisterParameterDeclarationCallback = _libs["esminiLib"].get("SE_RegisterParameterDeclarationCallback", "cdecl")
    SE_RegisterParameterDeclarationCallback.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(None)), POINTER(None)]
    SE_RegisterParameterDeclarationCallback.restype = None

    ctypes_SE_RegisterParameterDeclarationCallback = SE_RegisterParameterDeclarationCallback
    def SE_RegisterParameterDeclarationCallback(fun_1 : CFUNCTYPE(UNCHECKED(None), POINTER(None)), user_data : POINTER(None)) -> None : 
        return ctypes_SE_RegisterParameterDeclarationCallback(fun_1, user_data)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 312
if _libs["esminiLib"].has("SE_SetOSITolerances", "cdecl"):
    SE_SetOSITolerances = _libs["esminiLib"].get("SE_SetOSITolerances", "cdecl")
    SE_SetOSITolerances.argtypes = [c_double, c_double]
    SE_SetOSITolerances.restype = c_int

    ctypes_SE_SetOSITolerances = SE_SetOSITolerances
    def SE_SetOSITolerances(maxLongitudinalDistance : c_double, maxLateralDeviation : c_double) -> c_int : 
        return ctypes_SE_SetOSITolerances(maxLongitudinalDistance, maxLateralDeviation)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 319
if _libs["esminiLib"].has("SE_SetParameterDistribution", "cdecl"):
    SE_SetParameterDistribution = _libs["esminiLib"].get("SE_SetParameterDistribution", "cdecl")
    SE_SetParameterDistribution.argtypes = [String]
    SE_SetParameterDistribution.restype = c_int

    ctypes_SE_SetParameterDistribution = SE_SetParameterDistribution
    def SE_SetParameterDistribution(filename : String) -> c_int : 
        return ctypes_SE_SetParameterDistribution(filename)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 324
if _libs["esminiLib"].has("SE_ResetParameterDistribution", "cdecl"):
    SE_ResetParameterDistribution = _libs["esminiLib"].get("SE_ResetParameterDistribution", "cdecl")
    SE_ResetParameterDistribution.argtypes = []
    SE_ResetParameterDistribution.restype = None

    ctypes_SE_ResetParameterDistribution = SE_ResetParameterDistribution
    def SE_ResetParameterDistribution() -> None : 
        return ctypes_SE_ResetParameterDistribution()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 330
if _libs["esminiLib"].has("SE_GetNumberOfPermutations", "cdecl"):
    SE_GetNumberOfPermutations = _libs["esminiLib"].get("SE_GetNumberOfPermutations", "cdecl")
    SE_GetNumberOfPermutations.argtypes = []
    SE_GetNumberOfPermutations.restype = c_int

    ctypes_SE_GetNumberOfPermutations = SE_GetNumberOfPermutations
    def SE_GetNumberOfPermutations() -> c_int : 
        return ctypes_SE_GetNumberOfPermutations()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 336
if _libs["esminiLib"].has("SE_SelectPermutation", "cdecl"):
    SE_SelectPermutation = _libs["esminiLib"].get("SE_SelectPermutation", "cdecl")
    SE_SelectPermutation.argtypes = [c_int]
    SE_SelectPermutation.restype = c_int

    ctypes_SE_SelectPermutation = SE_SelectPermutation
    def SE_SelectPermutation(index : c_int) -> c_int : 
        return ctypes_SE_SelectPermutation(index)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 342
if _libs["esminiLib"].has("SE_GetPermutationIndex", "cdecl"):
    SE_GetPermutationIndex = _libs["esminiLib"].get("SE_GetPermutationIndex", "cdecl")
    SE_GetPermutationIndex.argtypes = []
    SE_GetPermutationIndex.restype = c_int

    ctypes_SE_GetPermutationIndex = SE_GetPermutationIndex
    def SE_GetPermutationIndex() -> c_int : 
        return ctypes_SE_GetPermutationIndex()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 362
if _libs["esminiLib"].has("SE_Init", "cdecl"):
    SE_Init = _libs["esminiLib"].get("SE_Init", "cdecl")
    SE_Init.argtypes = [String, c_int, c_int, c_int, c_int]
    SE_Init.restype = c_int

    ctypes_SE_Init = SE_Init
    def SE_Init(oscFilename : String, disable_ctrls : c_int, use_viewer : c_int, threads : c_int, record : c_int) -> c_int : 
        return ctypes_SE_Init(oscFilename, disable_ctrls, use_viewer, threads, record)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 382
if _libs["esminiLib"].has("SE_InitWithString", "cdecl"):
    SE_InitWithString = _libs["esminiLib"].get("SE_InitWithString", "cdecl")
    SE_InitWithString.argtypes = [String, c_int, c_int, c_int, c_int]
    SE_InitWithString.restype = c_int

    ctypes_SE_InitWithString = SE_InitWithString
    def SE_InitWithString(oscAsXMLString : String, disable_ctrls : c_int, use_viewer : c_int, threads : c_int, record : c_int) -> c_int : 
        return ctypes_SE_InitWithString(oscAsXMLString, disable_ctrls, use_viewer, threads, record)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 390
if _libs["esminiLib"].has("SE_InitWithArgs", "cdecl"):
    SE_InitWithArgs = _libs["esminiLib"].get("SE_InitWithArgs", "cdecl")
    SE_InitWithArgs.argtypes = [c_int, POINTER(POINTER(c_char))]
    SE_InitWithArgs.restype = c_int

    ctypes_SE_InitWithArgs = SE_InitWithArgs
    def SE_InitWithArgs(argc : c_int, argv : POINTER(POINTER(c_char))) -> c_int : 
        return ctypes_SE_InitWithArgs(argc, argv)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 397
if _libs["esminiLib"].has("SE_StepDT", "cdecl"):
    SE_StepDT = _libs["esminiLib"].get("SE_StepDT", "cdecl")
    SE_StepDT.argtypes = [c_float]
    SE_StepDT.restype = c_int

    ctypes_SE_StepDT = SE_StepDT
    def SE_StepDT(dt : c_float) -> c_int : 
        return ctypes_SE_StepDT(dt)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 403
if _libs["esminiLib"].has("SE_Step", "cdecl"):
    SE_Step = _libs["esminiLib"].get("SE_Step", "cdecl")
    SE_Step.argtypes = []
    SE_Step.restype = c_int

    ctypes_SE_Step = SE_Step
    def SE_Step() -> c_int : 
        return ctypes_SE_Step()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 408
if _libs["esminiLib"].has("SE_Close", "cdecl"):
    SE_Close = _libs["esminiLib"].get("SE_Close", "cdecl")
    SE_Close.argtypes = []
    SE_Close.restype = None

    ctypes_SE_Close = SE_Close
    def SE_Close() -> None : 
        return ctypes_SE_Close()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 414
if _libs["esminiLib"].has("SE_LogToConsole", "cdecl"):
    SE_LogToConsole = _libs["esminiLib"].get("SE_LogToConsole", "cdecl")
    SE_LogToConsole.argtypes = [c_bool]
    SE_LogToConsole.restype = None

    ctypes_SE_LogToConsole = SE_LogToConsole
    def SE_LogToConsole(mode : c_bool) -> None : 
        return ctypes_SE_LogToConsole(mode)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 420
if _libs["esminiLib"].has("SE_CollisionDetection", "cdecl"):
    SE_CollisionDetection = _libs["esminiLib"].get("SE_CollisionDetection", "cdecl")
    SE_CollisionDetection.argtypes = [c_bool]
    SE_CollisionDetection.restype = None

    ctypes_SE_CollisionDetection = SE_CollisionDetection
    def SE_CollisionDetection(mode : c_bool) -> None : 
        return ctypes_SE_CollisionDetection(mode)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 425
if _libs["esminiLib"].has("SE_GetSimulationTime", "cdecl"):
    SE_GetSimulationTime = _libs["esminiLib"].get("SE_GetSimulationTime", "cdecl")
    SE_GetSimulationTime.argtypes = []
    SE_GetSimulationTime.restype = c_float

    ctypes_SE_GetSimulationTime = SE_GetSimulationTime
    def SE_GetSimulationTime() -> c_float : 
        return ctypes_SE_GetSimulationTime()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 430
if _libs["esminiLib"].has("SE_GetSimulationTimeDouble", "cdecl"):
    SE_GetSimulationTimeDouble = _libs["esminiLib"].get("SE_GetSimulationTimeDouble", "cdecl")
    SE_GetSimulationTimeDouble.argtypes = []
    SE_GetSimulationTimeDouble.restype = c_double

    ctypes_SE_GetSimulationTimeDouble = SE_GetSimulationTimeDouble
    def SE_GetSimulationTimeDouble() -> c_double : 
        return ctypes_SE_GetSimulationTimeDouble()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 437
if _libs["esminiLib"].has("SE_GetSimTimeStep", "cdecl"):
    SE_GetSimTimeStep = _libs["esminiLib"].get("SE_GetSimTimeStep", "cdecl")
    SE_GetSimTimeStep.argtypes = []
    SE_GetSimTimeStep.restype = c_float

    ctypes_SE_GetSimTimeStep = SE_GetSimTimeStep
    def SE_GetSimTimeStep() -> c_float : 
        return ctypes_SE_GetSimTimeStep()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 443
if _libs["esminiLib"].has("SE_GetQuitFlag", "cdecl"):
    SE_GetQuitFlag = _libs["esminiLib"].get("SE_GetQuitFlag", "cdecl")
    SE_GetQuitFlag.argtypes = []
    SE_GetQuitFlag.restype = c_int

    ctypes_SE_GetQuitFlag = SE_GetQuitFlag
    def SE_GetQuitFlag() -> c_int : 
        return ctypes_SE_GetQuitFlag()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 449
if _libs["esminiLib"].has("SE_GetPauseFlag", "cdecl"):
    SE_GetPauseFlag = _libs["esminiLib"].get("SE_GetPauseFlag", "cdecl")
    SE_GetPauseFlag.argtypes = []
    SE_GetPauseFlag.restype = c_int

    ctypes_SE_GetPauseFlag = SE_GetPauseFlag
    def SE_GetPauseFlag() -> c_int : 
        return ctypes_SE_GetPauseFlag()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 455
if _libs["esminiLib"].has("SE_GetODRFilename", "cdecl"):
    SE_GetODRFilename = _libs["esminiLib"].get("SE_GetODRFilename", "cdecl")
    SE_GetODRFilename.argtypes = []
    SE_GetODRFilename.restype = c_char_p

    ctypes_SE_GetODRFilename = SE_GetODRFilename
    def SE_GetODRFilename() -> c_char_p : 
        return ctypes_SE_GetODRFilename()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 461
if _libs["esminiLib"].has("SE_GetSceneGraphFilename", "cdecl"):
    SE_GetSceneGraphFilename = _libs["esminiLib"].get("SE_GetSceneGraphFilename", "cdecl")
    SE_GetSceneGraphFilename.argtypes = []
    SE_GetSceneGraphFilename.restype = c_char_p

    ctypes_SE_GetSceneGraphFilename = SE_GetSceneGraphFilename
    def SE_GetSceneGraphFilename() -> c_char_p : 
        return ctypes_SE_GetSceneGraphFilename()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 467
if _libs["esminiLib"].has("SE_GetNumberOfParameters", "cdecl"):
    SE_GetNumberOfParameters = _libs["esminiLib"].get("SE_GetNumberOfParameters", "cdecl")
    SE_GetNumberOfParameters.argtypes = []
    SE_GetNumberOfParameters.restype = c_int

    ctypes_SE_GetNumberOfParameters = SE_GetNumberOfParameters
    def SE_GetNumberOfParameters() -> c_int : 
        return ctypes_SE_GetNumberOfParameters()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 475
if _libs["esminiLib"].has("SE_GetParameterName", "cdecl"):
    SE_GetParameterName = _libs["esminiLib"].get("SE_GetParameterName", "cdecl")
    SE_GetParameterName.argtypes = [c_int, POINTER(c_int)]
    SE_GetParameterName.restype = c_char_p

    ctypes_SE_GetParameterName = SE_GetParameterName
    def SE_GetParameterName(index : c_int, type : POINTER(c_int)) -> c_char_p : 
        return ctypes_SE_GetParameterName(index, type)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 482
if _libs["esminiLib"].has("SE_GetNumberOfProperties", "cdecl"):
    SE_GetNumberOfProperties = _libs["esminiLib"].get("SE_GetNumberOfProperties", "cdecl")
    SE_GetNumberOfProperties.argtypes = [c_int]
    SE_GetNumberOfProperties.restype = c_int

    ctypes_SE_GetNumberOfProperties = SE_GetNumberOfProperties
    def SE_GetNumberOfProperties(index : c_int) -> c_int : 
        return ctypes_SE_GetNumberOfProperties(index)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 489
if _libs["esminiLib"].has("SE_GetObjectPropertyName", "cdecl"):
    SE_GetObjectPropertyName = _libs["esminiLib"].get("SE_GetObjectPropertyName", "cdecl")
    SE_GetObjectPropertyName.argtypes = [c_int, c_int]
    SE_GetObjectPropertyName.restype = c_char_p

    ctypes_SE_GetObjectPropertyName = SE_GetObjectPropertyName
    def SE_GetObjectPropertyName(index : c_int, propertyIndex : c_int) -> c_char_p : 
        return ctypes_SE_GetObjectPropertyName(index, propertyIndex)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 496
if _libs["esminiLib"].has("SE_GetObjectPropertyValue", "cdecl"):
    SE_GetObjectPropertyValue = _libs["esminiLib"].get("SE_GetObjectPropertyValue", "cdecl")
    SE_GetObjectPropertyValue.argtypes = [c_int, String]
    SE_GetObjectPropertyValue.restype = c_char_p

    ctypes_SE_GetObjectPropertyValue = SE_GetObjectPropertyValue
    def SE_GetObjectPropertyValue(index : c_int, objectPropertyName : String) -> c_char_p : 
        return ctypes_SE_GetObjectPropertyValue(index, objectPropertyName)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 503
if _libs["esminiLib"].has("SE_SetParameter", "cdecl"):
    SE_SetParameter = _libs["esminiLib"].get("SE_SetParameter", "cdecl")
    SE_SetParameter.argtypes = [SE_Parameter]
    SE_SetParameter.restype = c_int

    ctypes_SE_SetParameter = SE_SetParameter
    def SE_SetParameter(parameter : SE_Parameter) -> c_int : 
        return ctypes_SE_SetParameter(parameter)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 510
if _libs["esminiLib"].has("SE_GetParameter", "cdecl"):
    SE_GetParameter = _libs["esminiLib"].get("SE_GetParameter", "cdecl")
    SE_GetParameter.argtypes = [POINTER(SE_Parameter)]
    SE_GetParameter.restype = c_int

    ctypes_SE_GetParameter = SE_GetParameter
    def SE_GetParameter(parameter : POINTER(SE_Parameter)) -> c_int : 
        return ctypes_SE_GetParameter(parameter)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 517
if _libs["esminiLib"].has("SE_GetParameterInt", "cdecl"):
    SE_GetParameterInt = _libs["esminiLib"].get("SE_GetParameterInt", "cdecl")
    SE_GetParameterInt.argtypes = [String, POINTER(c_int)]
    SE_GetParameterInt.restype = c_int

    ctypes_SE_GetParameterInt = SE_GetParameterInt
    def SE_GetParameterInt(parameterName : String, value : POINTER(c_int)) -> c_int : 
        return ctypes_SE_GetParameterInt(parameterName, value)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 524
if _libs["esminiLib"].has("SE_GetParameterDouble", "cdecl"):
    SE_GetParameterDouble = _libs["esminiLib"].get("SE_GetParameterDouble", "cdecl")
    SE_GetParameterDouble.argtypes = [String, POINTER(c_double)]
    SE_GetParameterDouble.restype = c_int

    ctypes_SE_GetParameterDouble = SE_GetParameterDouble
    def SE_GetParameterDouble(parameterName : String, value : POINTER(c_double)) -> c_int : 
        return ctypes_SE_GetParameterDouble(parameterName, value)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 531
if _libs["esminiLib"].has("SE_GetParameterString", "cdecl"):
    SE_GetParameterString = _libs["esminiLib"].get("SE_GetParameterString", "cdecl")
    SE_GetParameterString.argtypes = [String, POINTER(POINTER(c_char))]
    SE_GetParameterString.restype = c_int

    ctypes_SE_GetParameterString = SE_GetParameterString
    def SE_GetParameterString(parameterName : String, value : POINTER(POINTER(c_char))) -> c_int : 
        return ctypes_SE_GetParameterString(parameterName, value)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 538
if _libs["esminiLib"].has("SE_GetParameterBool", "cdecl"):
    SE_GetParameterBool = _libs["esminiLib"].get("SE_GetParameterBool", "cdecl")
    SE_GetParameterBool.argtypes = [String, POINTER(c_bool)]
    SE_GetParameterBool.restype = c_int

    ctypes_SE_GetParameterBool = SE_GetParameterBool
    def SE_GetParameterBool(parameterName : String, value : POINTER(c_bool)) -> c_int : 
        return ctypes_SE_GetParameterBool(parameterName, value)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 546
if _libs["esminiLib"].has("SE_SetParameterInt", "cdecl"):
    SE_SetParameterInt = _libs["esminiLib"].get("SE_SetParameterInt", "cdecl")
    SE_SetParameterInt.argtypes = [String, c_int]
    SE_SetParameterInt.restype = c_int

    ctypes_SE_SetParameterInt = SE_SetParameterInt
    def SE_SetParameterInt(parameterName : String, value : c_int) -> c_int : 
        return ctypes_SE_SetParameterInt(parameterName, value)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 554
if _libs["esminiLib"].has("SE_SetParameterDouble", "cdecl"):
    SE_SetParameterDouble = _libs["esminiLib"].get("SE_SetParameterDouble", "cdecl")
    SE_SetParameterDouble.argtypes = [String, c_double]
    SE_SetParameterDouble.restype = c_int

    ctypes_SE_SetParameterDouble = SE_SetParameterDouble
    def SE_SetParameterDouble(parameterName : String, value : c_double) -> c_int : 
        return ctypes_SE_SetParameterDouble(parameterName, value)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 562
if _libs["esminiLib"].has("SE_SetParameterString", "cdecl"):
    SE_SetParameterString = _libs["esminiLib"].get("SE_SetParameterString", "cdecl")
    SE_SetParameterString.argtypes = [String, String]
    SE_SetParameterString.restype = c_int

    ctypes_SE_SetParameterString = SE_SetParameterString
    def SE_SetParameterString(parameterName : String, value : String) -> c_int : 
        return ctypes_SE_SetParameterString(parameterName, value)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 570
if _libs["esminiLib"].has("SE_SetParameterBool", "cdecl"):
    SE_SetParameterBool = _libs["esminiLib"].get("SE_SetParameterBool", "cdecl")
    SE_SetParameterBool.argtypes = [String, c_bool]
    SE_SetParameterBool.restype = c_int

    ctypes_SE_SetParameterBool = SE_SetParameterBool
    def SE_SetParameterBool(parameterName : String, value : c_bool) -> c_int : 
        return ctypes_SE_SetParameterBool(parameterName, value)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 572
if _libs["esminiLib"].has("SE_SetVariable", "cdecl"):
    SE_SetVariable = _libs["esminiLib"].get("SE_SetVariable", "cdecl")
    SE_SetVariable.argtypes = [SE_Variable]
    SE_SetVariable.restype = c_int

    ctypes_SE_SetVariable = SE_SetVariable
    def SE_SetVariable(variable : SE_Variable) -> c_int : 
        return ctypes_SE_SetVariable(variable)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 579
if _libs["esminiLib"].has("SE_GetVariable", "cdecl"):
    SE_GetVariable = _libs["esminiLib"].get("SE_GetVariable", "cdecl")
    SE_GetVariable.argtypes = [POINTER(SE_Variable)]
    SE_GetVariable.restype = c_int

    ctypes_SE_GetVariable = SE_GetVariable
    def SE_GetVariable(variable : POINTER(SE_Variable)) -> c_int : 
        return ctypes_SE_GetVariable(variable)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 586
if _libs["esminiLib"].has("SE_GetVariableInt", "cdecl"):
    SE_GetVariableInt = _libs["esminiLib"].get("SE_GetVariableInt", "cdecl")
    SE_GetVariableInt.argtypes = [String, POINTER(c_int)]
    SE_GetVariableInt.restype = c_int

    ctypes_SE_GetVariableInt = SE_GetVariableInt
    def SE_GetVariableInt(variableName : String, value : POINTER(c_int)) -> c_int : 
        return ctypes_SE_GetVariableInt(variableName, value)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 593
if _libs["esminiLib"].has("SE_GetVariableDouble", "cdecl"):
    SE_GetVariableDouble = _libs["esminiLib"].get("SE_GetVariableDouble", "cdecl")
    SE_GetVariableDouble.argtypes = [String, POINTER(c_double)]
    SE_GetVariableDouble.restype = c_int

    ctypes_SE_GetVariableDouble = SE_GetVariableDouble
    def SE_GetVariableDouble(variableName : String, value : POINTER(c_double)) -> c_int : 
        return ctypes_SE_GetVariableDouble(variableName, value)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 600
if _libs["esminiLib"].has("SE_GetVariableString", "cdecl"):
    SE_GetVariableString = _libs["esminiLib"].get("SE_GetVariableString", "cdecl")
    SE_GetVariableString.argtypes = [String, POINTER(POINTER(c_char))]
    SE_GetVariableString.restype = c_int

    ctypes_SE_GetVariableString = SE_GetVariableString
    def SE_GetVariableString(variableName : String, value : POINTER(POINTER(c_char))) -> c_int : 
        return ctypes_SE_GetVariableString(variableName, value)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 607
if _libs["esminiLib"].has("SE_GetVariableBool", "cdecl"):
    SE_GetVariableBool = _libs["esminiLib"].get("SE_GetVariableBool", "cdecl")
    SE_GetVariableBool.argtypes = [String, POINTER(c_bool)]
    SE_GetVariableBool.restype = c_int

    ctypes_SE_GetVariableBool = SE_GetVariableBool
    def SE_GetVariableBool(variableName : String, value : POINTER(c_bool)) -> c_int : 
        return ctypes_SE_GetVariableBool(variableName, value)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 615
if _libs["esminiLib"].has("SE_SetVariableInt", "cdecl"):
    SE_SetVariableInt = _libs["esminiLib"].get("SE_SetVariableInt", "cdecl")
    SE_SetVariableInt.argtypes = [String, c_int]
    SE_SetVariableInt.restype = c_int

    ctypes_SE_SetVariableInt = SE_SetVariableInt
    def SE_SetVariableInt(variableName : String, value : c_int) -> c_int : 
        return ctypes_SE_SetVariableInt(variableName, value)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 623
if _libs["esminiLib"].has("SE_SetVariableDouble", "cdecl"):
    SE_SetVariableDouble = _libs["esminiLib"].get("SE_SetVariableDouble", "cdecl")
    SE_SetVariableDouble.argtypes = [String, c_double]
    SE_SetVariableDouble.restype = c_int

    ctypes_SE_SetVariableDouble = SE_SetVariableDouble
    def SE_SetVariableDouble(variableName : String, value : c_double) -> c_int : 
        return ctypes_SE_SetVariableDouble(variableName, value)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 631
if _libs["esminiLib"].has("SE_SetVariableString", "cdecl"):
    SE_SetVariableString = _libs["esminiLib"].get("SE_SetVariableString", "cdecl")
    SE_SetVariableString.argtypes = [String, String]
    SE_SetVariableString.restype = c_int

    ctypes_SE_SetVariableString = SE_SetVariableString
    def SE_SetVariableString(variableName : String, value : String) -> c_int : 
        return ctypes_SE_SetVariableString(variableName, value)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 639
if _libs["esminiLib"].has("SE_SetVariableBool", "cdecl"):
    SE_SetVariableBool = _libs["esminiLib"].get("SE_SetVariableBool", "cdecl")
    SE_SetVariableBool.argtypes = [String, c_bool]
    SE_SetVariableBool.restype = c_int

    ctypes_SE_SetVariableBool = SE_SetVariableBool
    def SE_SetVariableBool(variableName : String, value : c_bool) -> c_int : 
        return ctypes_SE_SetVariableBool(variableName, value)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 641
if _libs["esminiLib"].has("SE_GetODRManager", "cdecl"):
    SE_GetODRManager = _libs["esminiLib"].get("SE_GetODRManager", "cdecl")
    SE_GetODRManager.argtypes = []
    SE_GetODRManager.restype = POINTER(c_ubyte)
    SE_GetODRManager.errcheck = lambda v,*a : cast(v, c_void_p)

    ctypes_SE_GetODRManager = SE_GetODRManager
    def SE_GetODRManager() -> POINTER(c_ubyte) : 
        return ctypes_SE_GetODRManager()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 652
if _libs["esminiLib"].has("SE_SetAlignMode", "cdecl"):
    SE_SetAlignMode = _libs["esminiLib"].get("SE_SetAlignMode", "cdecl")
    SE_SetAlignMode.argtypes = [c_int, c_int]
    SE_SetAlignMode.restype = None

    ctypes_SE_SetAlignMode = SE_SetAlignMode
    def SE_SetAlignMode(object_id : c_int, mode : c_int) -> None : 
        return ctypes_SE_SetAlignMode(object_id, mode)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 663
if _libs["esminiLib"].has("SE_SetAlignModeH", "cdecl"):
    SE_SetAlignModeH = _libs["esminiLib"].get("SE_SetAlignModeH", "cdecl")
    SE_SetAlignModeH.argtypes = [c_int, c_int]
    SE_SetAlignModeH.restype = None

    ctypes_SE_SetAlignModeH = SE_SetAlignModeH
    def SE_SetAlignModeH(object_id : c_int, mode : c_int) -> None : 
        return ctypes_SE_SetAlignModeH(object_id, mode)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 675
if _libs["esminiLib"].has("SE_SetAlignModeP", "cdecl"):
    SE_SetAlignModeP = _libs["esminiLib"].get("SE_SetAlignModeP", "cdecl")
    SE_SetAlignModeP.argtypes = [c_int, c_int]
    SE_SetAlignModeP.restype = None

    ctypes_SE_SetAlignModeP = SE_SetAlignModeP
    def SE_SetAlignModeP(object_id : c_int, mode : c_int) -> None : 
        return ctypes_SE_SetAlignModeP(object_id, mode)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 685
if _libs["esminiLib"].has("SE_SetAlignModeR", "cdecl"):
    SE_SetAlignModeR = _libs["esminiLib"].get("SE_SetAlignModeR", "cdecl")
    SE_SetAlignModeR.argtypes = [c_int, c_int]
    SE_SetAlignModeR.restype = None

    ctypes_SE_SetAlignModeR = SE_SetAlignModeR
    def SE_SetAlignModeR(object_id : c_int, mode : c_int) -> None : 
        return ctypes_SE_SetAlignModeR(object_id, mode)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 696
if _libs["esminiLib"].has("SE_SetAlignModeZ", "cdecl"):
    SE_SetAlignModeZ = _libs["esminiLib"].get("SE_SetAlignModeZ", "cdecl")
    SE_SetAlignModeZ.argtypes = [c_int, c_int]
    SE_SetAlignModeZ.restype = None

    ctypes_SE_SetAlignModeZ = SE_SetAlignModeZ
    def SE_SetAlignModeZ(object_id : c_int, mode : c_int) -> None : 
        return ctypes_SE_SetAlignModeZ(object_id, mode)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 708
if _libs["esminiLib"].has("SE_AddObject", "cdecl"):
    SE_AddObject = _libs["esminiLib"].get("SE_AddObject", "cdecl")
    SE_AddObject.argtypes = [String, c_int, c_int, c_int, c_int]
    SE_AddObject.restype = c_int

    ctypes_SE_AddObject = SE_AddObject
    def SE_AddObject(object_name : String, object_type : c_int, object_category : c_int, object_role : c_int, model_id : c_int) -> c_int : 
        return ctypes_SE_AddObject(object_name, object_type, object_category, object_role, model_id)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 715
if _libs["esminiLib"].has("SE_DeleteObject", "cdecl"):
    SE_DeleteObject = _libs["esminiLib"].get("SE_DeleteObject", "cdecl")
    SE_DeleteObject.argtypes = [c_int]
    SE_DeleteObject.restype = c_int

    ctypes_SE_DeleteObject = SE_DeleteObject
    def SE_DeleteObject(object_id : c_int) -> c_int : 
        return ctypes_SE_DeleteObject(object_id)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 729
if _libs["esminiLib"].has("SE_ReportObjectPos", "cdecl"):
    SE_ReportObjectPos = _libs["esminiLib"].get("SE_ReportObjectPos", "cdecl")
    SE_ReportObjectPos.argtypes = [c_int, c_float, c_float, c_float, c_float, c_float, c_float, c_float]
    SE_ReportObjectPos.restype = c_int

    ctypes_SE_ReportObjectPos = SE_ReportObjectPos
    def SE_ReportObjectPos(object_id : c_int, timestamp : c_float, x : c_float, y : c_float, z : c_float, h : c_float, p : c_float, r : c_float) -> c_int : 
        return ctypes_SE_ReportObjectPos(object_id, timestamp, x, y, z, h, p, r)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 741
if _libs["esminiLib"].has("SE_ReportObjectPosXYH", "cdecl"):
    SE_ReportObjectPosXYH = _libs["esminiLib"].get("SE_ReportObjectPosXYH", "cdecl")
    SE_ReportObjectPosXYH.argtypes = [c_int, c_float, c_float, c_float, c_float]
    SE_ReportObjectPosXYH.restype = c_int

    ctypes_SE_ReportObjectPosXYH = SE_ReportObjectPosXYH
    def SE_ReportObjectPosXYH(object_id : c_int, timestamp : c_float, x : c_float, y : c_float, h : c_float) -> c_int : 
        return ctypes_SE_ReportObjectPosXYH(object_id, timestamp, x, y, h)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 753
if _libs["esminiLib"].has("SE_ReportObjectRoadPos", "cdecl"):
    SE_ReportObjectRoadPos = _libs["esminiLib"].get("SE_ReportObjectRoadPos", "cdecl")
    SE_ReportObjectRoadPos.argtypes = [c_int, c_float, c_int, c_int, c_float, c_float]
    SE_ReportObjectRoadPos.restype = c_int

    ctypes_SE_ReportObjectRoadPos = SE_ReportObjectRoadPos
    def SE_ReportObjectRoadPos(object_id : c_int, timestamp : c_float, roadId : c_int, laneId : c_int, laneOffset : c_float, s : c_float) -> c_int : 
        return ctypes_SE_ReportObjectRoadPos(object_id, timestamp, roadId, laneId, laneOffset, s)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 761
if _libs["esminiLib"].has("SE_ReportObjectSpeed", "cdecl"):
    SE_ReportObjectSpeed = _libs["esminiLib"].get("SE_ReportObjectSpeed", "cdecl")
    SE_ReportObjectSpeed.argtypes = [c_int, c_float]
    SE_ReportObjectSpeed.restype = c_int

    ctypes_SE_ReportObjectSpeed = SE_ReportObjectSpeed
    def SE_ReportObjectSpeed(object_id : c_int, speed : c_float) -> c_int : 
        return ctypes_SE_ReportObjectSpeed(object_id, speed)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 769
if _libs["esminiLib"].has("SE_ReportObjectLateralPosition", "cdecl"):
    SE_ReportObjectLateralPosition = _libs["esminiLib"].get("SE_ReportObjectLateralPosition", "cdecl")
    SE_ReportObjectLateralPosition.argtypes = [c_int, c_float]
    SE_ReportObjectLateralPosition.restype = c_int

    ctypes_SE_ReportObjectLateralPosition = SE_ReportObjectLateralPosition
    def SE_ReportObjectLateralPosition(object_id : c_int, t : c_float) -> c_int : 
        return ctypes_SE_ReportObjectLateralPosition(object_id, t)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 778
if _libs["esminiLib"].has("SE_ReportObjectLateralLanePosition", "cdecl"):
    SE_ReportObjectLateralLanePosition = _libs["esminiLib"].get("SE_ReportObjectLateralLanePosition", "cdecl")
    SE_ReportObjectLateralLanePosition.argtypes = [c_int, c_int, c_float]
    SE_ReportObjectLateralLanePosition.restype = c_int

    ctypes_SE_ReportObjectLateralLanePosition = SE_ReportObjectLateralLanePosition
    def SE_ReportObjectLateralLanePosition(object_id : c_int, laneId : c_int, laneOffset : c_float) -> c_int : 
        return ctypes_SE_ReportObjectLateralLanePosition(object_id, laneId, laneOffset)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 790
if _libs["esminiLib"].has("SE_ReportObjectVel", "cdecl"):
    SE_ReportObjectVel = _libs["esminiLib"].get("SE_ReportObjectVel", "cdecl")
    SE_ReportObjectVel.argtypes = [c_int, c_float, c_float, c_float, c_float]
    SE_ReportObjectVel.restype = c_int

    ctypes_SE_ReportObjectVel = SE_ReportObjectVel
    def SE_ReportObjectVel(object_id : c_int, timestamp : c_float, x_vel : c_float, y_vel : c_float, z_vel : c_float) -> c_int : 
        return ctypes_SE_ReportObjectVel(object_id, timestamp, x_vel, y_vel, z_vel)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 801
if _libs["esminiLib"].has("SE_ReportObjectAngularVel", "cdecl"):
    SE_ReportObjectAngularVel = _libs["esminiLib"].get("SE_ReportObjectAngularVel", "cdecl")
    SE_ReportObjectAngularVel.argtypes = [c_int, c_float, c_float, c_float, c_float]
    SE_ReportObjectAngularVel.restype = c_int

    ctypes_SE_ReportObjectAngularVel = SE_ReportObjectAngularVel
    def SE_ReportObjectAngularVel(object_id : c_int, timestamp : c_float, h_rate : c_float, p_rate : c_float, r_rate : c_float) -> c_int : 
        return ctypes_SE_ReportObjectAngularVel(object_id, timestamp, h_rate, p_rate, r_rate)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 812
if _libs["esminiLib"].has("SE_ReportObjectAcc", "cdecl"):
    SE_ReportObjectAcc = _libs["esminiLib"].get("SE_ReportObjectAcc", "cdecl")
    SE_ReportObjectAcc.argtypes = [c_int, c_float, c_float, c_float, c_float]
    SE_ReportObjectAcc.restype = c_int

    ctypes_SE_ReportObjectAcc = SE_ReportObjectAcc
    def SE_ReportObjectAcc(object_id : c_int, timestamp : c_float, x_acc : c_float, y_acc : c_float, z_acc : c_float) -> c_int : 
        return ctypes_SE_ReportObjectAcc(object_id, timestamp, x_acc, y_acc, z_acc)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 823
if _libs["esminiLib"].has("SE_ReportObjectAngularAcc", "cdecl"):
    SE_ReportObjectAngularAcc = _libs["esminiLib"].get("SE_ReportObjectAngularAcc", "cdecl")
    SE_ReportObjectAngularAcc.argtypes = [c_int, c_float, c_float, c_float, c_float]
    SE_ReportObjectAngularAcc.restype = c_int

    ctypes_SE_ReportObjectAngularAcc = SE_ReportObjectAngularAcc
    def SE_ReportObjectAngularAcc(object_id : c_int, timestamp : c_float, h_acc : c_float, p_acc : c_float, r_acc : c_float) -> c_int : 
        return ctypes_SE_ReportObjectAngularAcc(object_id, timestamp, h_acc, p_acc, r_acc)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 832
if _libs["esminiLib"].has("SE_ReportObjectWheelStatus", "cdecl"):
    SE_ReportObjectWheelStatus = _libs["esminiLib"].get("SE_ReportObjectWheelStatus", "cdecl")
    SE_ReportObjectWheelStatus.argtypes = [c_int, c_float, c_float]
    SE_ReportObjectWheelStatus.restype = c_int

    ctypes_SE_ReportObjectWheelStatus = SE_ReportObjectWheelStatus
    def SE_ReportObjectWheelStatus(object_id : c_int, rotation : c_float, angle : c_float) -> c_int : 
        return ctypes_SE_ReportObjectWheelStatus(object_id, rotation, angle)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 839
if _libs["esminiLib"].has("SE_SetLockOnLane", "cdecl"):
    SE_SetLockOnLane = _libs["esminiLib"].get("SE_SetLockOnLane", "cdecl")
    SE_SetLockOnLane.argtypes = [c_int, c_bool]
    SE_SetLockOnLane.restype = c_int

    ctypes_SE_SetLockOnLane = SE_SetLockOnLane
    def SE_SetLockOnLane(id : c_int, mode : c_bool) -> c_int : 
        return ctypes_SE_SetLockOnLane(id, mode)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 845
if _libs["esminiLib"].has("SE_GetNumberOfObjects", "cdecl"):
    SE_GetNumberOfObjects = _libs["esminiLib"].get("SE_GetNumberOfObjects", "cdecl")
    SE_GetNumberOfObjects.argtypes = []
    SE_GetNumberOfObjects.restype = c_int

    ctypes_SE_GetNumberOfObjects = SE_GetNumberOfObjects
    def SE_GetNumberOfObjects() -> c_int : 
        return ctypes_SE_GetNumberOfObjects()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 852
if _libs["esminiLib"].has("SE_GetId", "cdecl"):
    SE_GetId = _libs["esminiLib"].get("SE_GetId", "cdecl")
    SE_GetId.argtypes = [c_int]
    SE_GetId.restype = c_int

    ctypes_SE_GetId = SE_GetId
    def SE_GetId(index : c_int) -> c_int : 
        return ctypes_SE_GetId(index)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 859
if _libs["esminiLib"].has("SE_GetIdByName", "cdecl"):
    SE_GetIdByName = _libs["esminiLib"].get("SE_GetIdByName", "cdecl")
    SE_GetIdByName.argtypes = [String]
    SE_GetIdByName.restype = c_int

    ctypes_SE_GetIdByName = SE_GetIdByName
    def SE_GetIdByName(name : String) -> c_int : 
        return ctypes_SE_GetIdByName(name)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 867
if _libs["esminiLib"].has("SE_GetObjectState", "cdecl"):
    SE_GetObjectState = _libs["esminiLib"].get("SE_GetObjectState", "cdecl")
    SE_GetObjectState.argtypes = [c_int, POINTER(SE_ScenarioObjectState)]
    SE_GetObjectState.restype = c_int

    ctypes_SE_GetObjectState = SE_GetObjectState
    def SE_GetObjectState(object_id : c_int, state : POINTER(SE_ScenarioObjectState)) -> c_int : 
        return ctypes_SE_GetObjectState(object_id, state)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 875
if _libs["esminiLib"].has("SE_GetOverrideActionStatus", "cdecl"):
    SE_GetOverrideActionStatus = _libs["esminiLib"].get("SE_GetOverrideActionStatus", "cdecl")
    SE_GetOverrideActionStatus.argtypes = [c_int, POINTER(SE_OverrideActionList)]
    SE_GetOverrideActionStatus.restype = c_int

    ctypes_SE_GetOverrideActionStatus = SE_GetOverrideActionStatus
    def SE_GetOverrideActionStatus(objectId : c_int, list : POINTER(SE_OverrideActionList)) -> c_int : 
        return ctypes_SE_GetOverrideActionStatus(objectId, list)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 882
if _libs["esminiLib"].has("SE_GetObjectTypeName", "cdecl"):
    SE_GetObjectTypeName = _libs["esminiLib"].get("SE_GetObjectTypeName", "cdecl")
    SE_GetObjectTypeName.argtypes = [c_int]
    SE_GetObjectTypeName.restype = c_char_p

    ctypes_SE_GetObjectTypeName = SE_GetObjectTypeName
    def SE_GetObjectTypeName(object_id : c_int) -> c_char_p : 
        return ctypes_SE_GetObjectTypeName(object_id)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 889
if _libs["esminiLib"].has("SE_GetObjectName", "cdecl"):
    SE_GetObjectName = _libs["esminiLib"].get("SE_GetObjectName", "cdecl")
    SE_GetObjectName.argtypes = [c_int]
    SE_GetObjectName.restype = c_char_p

    ctypes_SE_GetObjectName = SE_GetObjectName
    def SE_GetObjectName(object_id : c_int) -> c_char_p : 
        return ctypes_SE_GetObjectName(object_id)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 896
if _libs["esminiLib"].has("SE_GetObjectModelFileName", "cdecl"):
    SE_GetObjectModelFileName = _libs["esminiLib"].get("SE_GetObjectModelFileName", "cdecl")
    SE_GetObjectModelFileName.argtypes = [c_int]
    SE_GetObjectModelFileName.restype = c_char_p

    ctypes_SE_GetObjectModelFileName = SE_GetObjectModelFileName
    def SE_GetObjectModelFileName(object_id : c_int) -> c_char_p : 
        return ctypes_SE_GetObjectModelFileName(object_id)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 903
if _libs["esminiLib"].has("SE_ObjectHasGhost", "cdecl"):
    SE_ObjectHasGhost = _libs["esminiLib"].get("SE_ObjectHasGhost", "cdecl")
    SE_ObjectHasGhost.argtypes = [c_int]
    SE_ObjectHasGhost.restype = c_int

    ctypes_SE_ObjectHasGhost = SE_ObjectHasGhost
    def SE_ObjectHasGhost(object_id : c_int) -> c_int : 
        return ctypes_SE_ObjectHasGhost(object_id)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 911
if _libs["esminiLib"].has("SE_GetObjectGhostState", "cdecl"):
    SE_GetObjectGhostState = _libs["esminiLib"].get("SE_GetObjectGhostState", "cdecl")
    SE_GetObjectGhostState.argtypes = [c_int, POINTER(SE_ScenarioObjectState)]
    SE_GetObjectGhostState.restype = c_int

    ctypes_SE_GetObjectGhostState = SE_GetObjectGhostState
    def SE_GetObjectGhostState(object_id : c_int, state : POINTER(SE_ScenarioObjectState)) -> c_int : 
        return ctypes_SE_GetObjectGhostState(object_id, state)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 918
if _libs["esminiLib"].has("SE_GetObjectNumberOfCollisions", "cdecl"):
    SE_GetObjectNumberOfCollisions = _libs["esminiLib"].get("SE_GetObjectNumberOfCollisions", "cdecl")
    SE_GetObjectNumberOfCollisions.argtypes = [c_int]
    SE_GetObjectNumberOfCollisions.restype = c_int

    ctypes_SE_GetObjectNumberOfCollisions = SE_GetObjectNumberOfCollisions
    def SE_GetObjectNumberOfCollisions(object_id : c_int) -> c_int : 
        return ctypes_SE_GetObjectNumberOfCollisions(object_id)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 926
if _libs["esminiLib"].has("SE_GetObjectCollision", "cdecl"):
    SE_GetObjectCollision = _libs["esminiLib"].get("SE_GetObjectCollision", "cdecl")
    SE_GetObjectCollision.argtypes = [c_int, c_int]
    SE_GetObjectCollision.restype = c_int

    ctypes_SE_GetObjectCollision = SE_GetObjectCollision
    def SE_GetObjectCollision(object_id : c_int, index : c_int) -> c_int : 
        return ctypes_SE_GetObjectCollision(object_id, index)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 935
if _libs["esminiLib"].has("SE_GetSpeedUnit", "cdecl"):
    SE_GetSpeedUnit = _libs["esminiLib"].get("SE_GetSpeedUnit", "cdecl")
    SE_GetSpeedUnit.argtypes = []
    SE_GetSpeedUnit.restype = c_int

    ctypes_SE_GetSpeedUnit = SE_GetSpeedUnit
    def SE_GetSpeedUnit() -> c_int : 
        return ctypes_SE_GetSpeedUnit()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 954
if _libs["esminiLib"].has("SE_GetRoadInfoAtDistance", "cdecl"):
    SE_GetRoadInfoAtDistance = _libs["esminiLib"].get("SE_GetRoadInfoAtDistance", "cdecl")
    SE_GetRoadInfoAtDistance.argtypes = [c_int, c_float, POINTER(SE_RoadInfo), c_int, c_bool]
    SE_GetRoadInfoAtDistance.restype = c_int

    ctypes_SE_GetRoadInfoAtDistance = SE_GetRoadInfoAtDistance
    def SE_GetRoadInfoAtDistance(object_id : c_int, lookahead_distance : c_float, data : POINTER(SE_RoadInfo), lookAheadMode : c_int, inRoadDrivingDirection : c_bool) -> c_int : 
        return ctypes_SE_GetRoadInfoAtDistance(object_id, lookahead_distance, data, lookAheadMode, inRoadDrivingDirection)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 968
if _libs["esminiLib"].has("SE_GetRoadInfoAlongGhostTrail", "cdecl"):
    SE_GetRoadInfoAlongGhostTrail = _libs["esminiLib"].get("SE_GetRoadInfoAlongGhostTrail", "cdecl")
    SE_GetRoadInfoAlongGhostTrail.argtypes = [c_int, c_float, POINTER(SE_RoadInfo), POINTER(c_float)]
    SE_GetRoadInfoAlongGhostTrail.restype = c_int

    ctypes_SE_GetRoadInfoAlongGhostTrail = SE_GetRoadInfoAlongGhostTrail
    def SE_GetRoadInfoAlongGhostTrail(object_id : c_int, lookahead_distance : c_float, data : POINTER(SE_RoadInfo), speed_ghost : POINTER(c_float)) -> c_int : 
        return ctypes_SE_GetRoadInfoAlongGhostTrail(object_id, lookahead_distance, data, speed_ghost)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 978
if _libs["esminiLib"].has("SE_GetRoadInfoGhostTrailTime", "cdecl"):
    SE_GetRoadInfoGhostTrailTime = _libs["esminiLib"].get("SE_GetRoadInfoGhostTrailTime", "cdecl")
    SE_GetRoadInfoGhostTrailTime.argtypes = [c_int, c_float, POINTER(SE_RoadInfo), POINTER(c_float)]
    SE_GetRoadInfoGhostTrailTime.restype = c_int

    ctypes_SE_GetRoadInfoGhostTrailTime = SE_GetRoadInfoGhostTrailTime
    def SE_GetRoadInfoGhostTrailTime(object_id : c_int, time : c_float, data : POINTER(SE_RoadInfo), speed_ghost : POINTER(c_float)) -> c_int : 
        return ctypes_SE_GetRoadInfoGhostTrailTime(object_id, time, data, speed_ghost)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 989
if _libs["esminiLib"].has("SE_GetDistanceToObject", "cdecl"):
    SE_GetDistanceToObject = _libs["esminiLib"].get("SE_GetDistanceToObject", "cdecl")
    SE_GetDistanceToObject.argtypes = [c_int, c_int, c_bool, POINTER(SE_PositionDiff)]
    SE_GetDistanceToObject.restype = c_int

    ctypes_SE_GetDistanceToObject = SE_GetDistanceToObject
    def SE_GetDistanceToObject(object_a_id : c_int, object_b_id : c_int, free_space : c_bool, pos_diff : POINTER(SE_PositionDiff)) -> c_int : 
        return ctypes_SE_GetDistanceToObject(object_a_id, object_b_id, free_space, pos_diff)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1004
if _libs["esminiLib"].has("SE_AddObjectSensor", "cdecl"):
    SE_AddObjectSensor = _libs["esminiLib"].get("SE_AddObjectSensor", "cdecl")
    SE_AddObjectSensor.argtypes = [c_int, c_float, c_float, c_float, c_float, c_float, c_float, c_float, c_int]
    SE_AddObjectSensor.restype = c_int

    ctypes_SE_AddObjectSensor = SE_AddObjectSensor
    def SE_AddObjectSensor(object_id : c_int, x : c_float, y : c_float, z : c_float, h : c_float, rangeNear : c_float, rangeFar : c_float, fovH : c_float, maxObj : c_int) -> c_int : 
        return ctypes_SE_AddObjectSensor(object_id, x, y, z, h, rangeNear, rangeFar, fovH, maxObj)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1011
if _libs["esminiLib"].has("SE_ViewSensorData", "cdecl"):
    SE_ViewSensorData = _libs["esminiLib"].get("SE_ViewSensorData", "cdecl")
    SE_ViewSensorData.argtypes = [c_int]
    SE_ViewSensorData.restype = c_int

    ctypes_SE_ViewSensorData = SE_ViewSensorData
    def SE_ViewSensorData(object_id : c_int) -> c_int : 
        return ctypes_SE_ViewSensorData(object_id)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1019
if _libs["esminiLib"].has("SE_FetchSensorObjectList", "cdecl"):
    SE_FetchSensorObjectList = _libs["esminiLib"].get("SE_FetchSensorObjectList", "cdecl")
    SE_FetchSensorObjectList.argtypes = [c_int, POINTER(c_int)]
    SE_FetchSensorObjectList.restype = c_int

    ctypes_SE_FetchSensorObjectList = SE_FetchSensorObjectList
    def SE_FetchSensorObjectList(sensor_id : c_int, list : POINTER(c_int)) -> c_int : 
        return ctypes_SE_FetchSensorObjectList(sensor_id, list)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1030
if _libs["esminiLib"].has("SE_RegisterObjectCallback", "cdecl"):
    SE_RegisterObjectCallback = _libs["esminiLib"].get("SE_RegisterObjectCallback", "cdecl")
    SE_RegisterObjectCallback.argtypes = [c_int, CFUNCTYPE(UNCHECKED(None), POINTER(SE_ScenarioObjectState), POINTER(None)), POINTER(None)]
    SE_RegisterObjectCallback.restype = None

    ctypes_SE_RegisterObjectCallback = SE_RegisterObjectCallback
    def SE_RegisterObjectCallback(object_id : c_int, fun_1 : CFUNCTYPE(UNCHECKED(None), POINTER(SE_ScenarioObjectState), POINTER(None)), user_data : POINTER(None)) -> None : 
        return ctypes_SE_RegisterObjectCallback(object_id, fun_1, user_data)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1038
if _libs["esminiLib"].has("SE_RegisterConditionCallback", "cdecl"):
    SE_RegisterConditionCallback = _libs["esminiLib"].get("SE_RegisterConditionCallback", "cdecl")
    SE_RegisterConditionCallback.argtypes = [CFUNCTYPE(UNCHECKED(None), String, c_double)]
    SE_RegisterConditionCallback.restype = None

    ctypes_SE_RegisterConditionCallback = SE_RegisterConditionCallback
    def SE_RegisterConditionCallback(fun_1 : CFUNCTYPE(UNCHECKED(None), String, c_double)) -> None : 
        return ctypes_SE_RegisterConditionCallback(fun_1)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1062
if _libs["esminiLib"].has("SE_RegisterStoryBoardElementStateChangeCallback", "cdecl"):
    SE_RegisterStoryBoardElementStateChangeCallback = _libs["esminiLib"].get("SE_RegisterStoryBoardElementStateChangeCallback", "cdecl")
    SE_RegisterStoryBoardElementStateChangeCallback.argtypes = [CFUNCTYPE(UNCHECKED(None), String, c_int, c_int)]
    SE_RegisterStoryBoardElementStateChangeCallback.restype = None

    ctypes_SE_RegisterStoryBoardElementStateChangeCallback = SE_RegisterStoryBoardElementStateChangeCallback
    def SE_RegisterStoryBoardElementStateChangeCallback(fun_1 : CFUNCTYPE(UNCHECKED(None), String, c_int, c_int)) -> None : 
        return ctypes_SE_RegisterStoryBoardElementStateChangeCallback(fun_1)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1069
if _libs["esminiLib"].has("SE_GetNumberOfRoadSigns", "cdecl"):
    SE_GetNumberOfRoadSigns = _libs["esminiLib"].get("SE_GetNumberOfRoadSigns", "cdecl")
    SE_GetNumberOfRoadSigns.argtypes = [c_int]
    SE_GetNumberOfRoadSigns.restype = c_int

    ctypes_SE_GetNumberOfRoadSigns = SE_GetNumberOfRoadSigns
    def SE_GetNumberOfRoadSigns(road_id : c_int) -> c_int : 
        return ctypes_SE_GetNumberOfRoadSigns(road_id)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1078
if _libs["esminiLib"].has("SE_GetRoadSign", "cdecl"):
    SE_GetRoadSign = _libs["esminiLib"].get("SE_GetRoadSign", "cdecl")
    SE_GetRoadSign.argtypes = [c_int, c_int, POINTER(SE_RoadSign)]
    SE_GetRoadSign.restype = c_int

    ctypes_SE_GetRoadSign = SE_GetRoadSign
    def SE_GetRoadSign(road_id : c_int, index : c_int, road_sign : POINTER(SE_RoadSign)) -> c_int : 
        return ctypes_SE_GetRoadSign(road_id, index, road_sign)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1086
if _libs["esminiLib"].has("SE_GetNumberOfRoadSignValidityRecords", "cdecl"):
    SE_GetNumberOfRoadSignValidityRecords = _libs["esminiLib"].get("SE_GetNumberOfRoadSignValidityRecords", "cdecl")
    SE_GetNumberOfRoadSignValidityRecords.argtypes = [c_int, c_int]
    SE_GetNumberOfRoadSignValidityRecords.restype = c_int

    ctypes_SE_GetNumberOfRoadSignValidityRecords = SE_GetNumberOfRoadSignValidityRecords
    def SE_GetNumberOfRoadSignValidityRecords(road_id : c_int, index : c_int) -> c_int : 
        return ctypes_SE_GetNumberOfRoadSignValidityRecords(road_id, index)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1096
if _libs["esminiLib"].has("SE_GetRoadSignValidityRecord", "cdecl"):
    SE_GetRoadSignValidityRecord = _libs["esminiLib"].get("SE_GetRoadSignValidityRecord", "cdecl")
    SE_GetRoadSignValidityRecord.argtypes = [c_int, c_int, c_int, POINTER(SE_RoadObjValidity)]
    SE_GetRoadSignValidityRecord.restype = c_int

    ctypes_SE_GetRoadSignValidityRecord = SE_GetRoadSignValidityRecord
    def SE_GetRoadSignValidityRecord(road_id : c_int, signIndex : c_int, validityIndex : c_int, validity : POINTER(SE_RoadObjValidity)) -> c_int : 
        return ctypes_SE_GetRoadSignValidityRecord(road_id, signIndex, validityIndex, validity)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1104
if _libs["esminiLib"].has("SE_OpenOSISocket", "cdecl"):
    SE_OpenOSISocket = _libs["esminiLib"].get("SE_OpenOSISocket", "cdecl")
    SE_OpenOSISocket.argtypes = [String]
    SE_OpenOSISocket.restype = c_int

    ctypes_SE_OpenOSISocket = SE_OpenOSISocket
    def SE_OpenOSISocket(ipaddr : String) -> c_int : 
        return ctypes_SE_OpenOSISocket(ipaddr)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1110
if _libs["esminiLib"].has("SE_DisableOSIFile", "cdecl"):
    SE_DisableOSIFile = _libs["esminiLib"].get("SE_DisableOSIFile", "cdecl")
    SE_DisableOSIFile.argtypes = []
    SE_DisableOSIFile.restype = None

    ctypes_SE_DisableOSIFile = SE_DisableOSIFile
    def SE_DisableOSIFile() -> None : 
        return ctypes_SE_DisableOSIFile()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1116
if _libs["esminiLib"].has("SE_EnableOSIFile", "cdecl"):
    SE_EnableOSIFile = _libs["esminiLib"].get("SE_EnableOSIFile", "cdecl")
    SE_EnableOSIFile.argtypes = [String]
    SE_EnableOSIFile.restype = None

    ctypes_SE_EnableOSIFile = SE_EnableOSIFile
    def SE_EnableOSIFile(filename : String) -> None : 
        return ctypes_SE_EnableOSIFile(filename)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1122
if _libs["esminiLib"].has("SE_FlushOSIFile", "cdecl"):
    SE_FlushOSIFile = _libs["esminiLib"].get("SE_FlushOSIFile", "cdecl")
    SE_FlushOSIFile.argtypes = []
    SE_FlushOSIFile.restype = None

    ctypes_SE_FlushOSIFile = SE_FlushOSIFile
    def SE_FlushOSIFile() -> None : 
        return ctypes_SE_FlushOSIFile()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1129
if _libs["esminiLib"].has("SE_ClearOSIGroundTruth", "cdecl"):
    SE_ClearOSIGroundTruth = _libs["esminiLib"].get("SE_ClearOSIGroundTruth", "cdecl")
    SE_ClearOSIGroundTruth.argtypes = []
    SE_ClearOSIGroundTruth.restype = c_int

    ctypes_SE_ClearOSIGroundTruth = SE_ClearOSIGroundTruth
    def SE_ClearOSIGroundTruth() -> c_int : 
        return ctypes_SE_ClearOSIGroundTruth()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1135
if _libs["esminiLib"].has("SE_UpdateOSIGroundTruth", "cdecl"):
    SE_UpdateOSIGroundTruth = _libs["esminiLib"].get("SE_UpdateOSIGroundTruth", "cdecl")
    SE_UpdateOSIGroundTruth.argtypes = []
    SE_UpdateOSIGroundTruth.restype = c_int

    ctypes_SE_UpdateOSIGroundTruth = SE_UpdateOSIGroundTruth
    def SE_UpdateOSIGroundTruth() -> c_int : 
        return ctypes_SE_UpdateOSIGroundTruth()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1141
if _libs["esminiLib"].has("SE_UpdateOSIStaticGroundTruth", "cdecl"):
    SE_UpdateOSIStaticGroundTruth = _libs["esminiLib"].get("SE_UpdateOSIStaticGroundTruth", "cdecl")
    SE_UpdateOSIStaticGroundTruth.argtypes = []
    SE_UpdateOSIStaticGroundTruth.restype = c_int

    ctypes_SE_UpdateOSIStaticGroundTruth = SE_UpdateOSIStaticGroundTruth
    def SE_UpdateOSIStaticGroundTruth() -> c_int : 
        return ctypes_SE_UpdateOSIStaticGroundTruth()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1154
if _libs["esminiLib"].has("SE_GetOSIGroundTruth", "cdecl"):
    SE_GetOSIGroundTruth = _libs["esminiLib"].get("SE_GetOSIGroundTruth", "cdecl")
    SE_GetOSIGroundTruth.argtypes = [POINTER(c_int)]
    SE_GetOSIGroundTruth.restype = c_char_p

    ctypes_SE_GetOSIGroundTruth = SE_GetOSIGroundTruth
    def SE_GetOSIGroundTruth(size : POINTER(c_int)) -> c_char_p : 
        return ctypes_SE_GetOSIGroundTruth(size)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1160
if _libs["esminiLib"].has("SE_GetOSIGroundTruthRaw", "cdecl"):
    SE_GetOSIGroundTruthRaw = _libs["esminiLib"].get("SE_GetOSIGroundTruthRaw", "cdecl")
    SE_GetOSIGroundTruthRaw.argtypes = []
    SE_GetOSIGroundTruthRaw.restype = c_char_p

    ctypes_SE_GetOSIGroundTruthRaw = SE_GetOSIGroundTruthRaw
    def SE_GetOSIGroundTruthRaw() -> c_char_p : 
        return ctypes_SE_GetOSIGroundTruthRaw()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1166
if _libs["esminiLib"].has("SE_SetOSISensorDataRaw", "cdecl"):
    SE_SetOSISensorDataRaw = _libs["esminiLib"].get("SE_SetOSISensorDataRaw", "cdecl")
    SE_SetOSISensorDataRaw.argtypes = [String]
    SE_SetOSISensorDataRaw.restype = c_int

    ctypes_SE_SetOSISensorDataRaw = SE_SetOSISensorDataRaw
    def SE_SetOSISensorDataRaw(sensordata : String) -> c_int : 
        return ctypes_SE_SetOSISensorDataRaw(sensordata)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1172
if _libs["esminiLib"].has("SE_GetOSISensorDataRaw", "cdecl"):
    SE_GetOSISensorDataRaw = _libs["esminiLib"].get("SE_GetOSISensorDataRaw", "cdecl")
    SE_GetOSISensorDataRaw.argtypes = []
    SE_GetOSISensorDataRaw.restype = c_char_p

    ctypes_SE_GetOSISensorDataRaw = SE_GetOSISensorDataRaw
    def SE_GetOSISensorDataRaw() -> c_char_p : 
        return ctypes_SE_GetOSISensorDataRaw()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1178
if _libs["esminiLib"].has("SE_GetOSIRoadLane", "cdecl"):
    SE_GetOSIRoadLane = _libs["esminiLib"].get("SE_GetOSIRoadLane", "cdecl")
    SE_GetOSIRoadLane.argtypes = [POINTER(c_int), c_int]
    SE_GetOSIRoadLane.restype = c_char_p

    ctypes_SE_GetOSIRoadLane = SE_GetOSIRoadLane
    def SE_GetOSIRoadLane(size : POINTER(c_int), object_id : c_int) -> c_char_p : 
        return ctypes_SE_GetOSIRoadLane(size, object_id)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1183
if _libs["esminiLib"].has("SE_GetOSILaneBoundary", "cdecl"):
    SE_GetOSILaneBoundary = _libs["esminiLib"].get("SE_GetOSILaneBoundary", "cdecl")
    SE_GetOSILaneBoundary.argtypes = [POINTER(c_int), c_int]
    SE_GetOSILaneBoundary.restype = c_char_p

    ctypes_SE_GetOSILaneBoundary = SE_GetOSILaneBoundary
    def SE_GetOSILaneBoundary(size : POINTER(c_int), global_id : c_int) -> c_char_p : 
        return ctypes_SE_GetOSILaneBoundary(size, global_id)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1190
if _libs["esminiLib"].has("SE_GetOSILaneBoundaryIds", "cdecl"):
    SE_GetOSILaneBoundaryIds = _libs["esminiLib"].get("SE_GetOSILaneBoundaryIds", "cdecl")
    SE_GetOSILaneBoundaryIds.argtypes = [c_int, POINTER(SE_LaneBoundaryId)]
    SE_GetOSILaneBoundaryIds.restype = None

    ctypes_SE_GetOSILaneBoundaryIds = SE_GetOSILaneBoundaryIds
    def SE_GetOSILaneBoundaryIds(object_id : c_int, ids : POINTER(SE_LaneBoundaryId)) -> None : 
        return ctypes_SE_GetOSILaneBoundaryIds(object_id, ids)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1196
if _libs["esminiLib"].has("SE_GetOSISensorDataRaw", "cdecl"):
    SE_GetOSISensorDataRaw = _libs["esminiLib"].get("SE_GetOSISensorDataRaw", "cdecl")
    SE_GetOSISensorDataRaw.argtypes = []
    SE_GetOSISensorDataRaw.restype = c_char_p

    ctypes_SE_GetOSISensorDataRaw = SE_GetOSISensorDataRaw
    def SE_GetOSISensorDataRaw() -> c_char_p : 
        return ctypes_SE_GetOSISensorDataRaw()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1203
if _libs["esminiLib"].has("SE_OSIFileOpen", "cdecl"):
    SE_OSIFileOpen = _libs["esminiLib"].get("SE_OSIFileOpen", "cdecl")
    SE_OSIFileOpen.argtypes = [String]
    SE_OSIFileOpen.restype = c_bool

    ctypes_SE_OSIFileOpen = SE_OSIFileOpen
    def SE_OSIFileOpen(filename : String) -> c_bool : 
        return ctypes_SE_OSIFileOpen(filename)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1218
if _libs["esminiLib"].has("SE_OSISetTimeStamp", "cdecl"):
    SE_OSISetTimeStamp = _libs["esminiLib"].get("SE_OSISetTimeStamp", "cdecl")
    SE_OSISetTimeStamp.argtypes = [c_ulonglong]
    SE_OSISetTimeStamp.restype = c_int

    ctypes_SE_OSISetTimeStamp = SE_OSISetTimeStamp
    def SE_OSISetTimeStamp(nanoseconds : c_ulonglong) -> c_int : 
        return ctypes_SE_OSISetTimeStamp(nanoseconds)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1222
if _libs["esminiLib"].has("SE_LogMessage", "cdecl"):
    SE_LogMessage = _libs["esminiLib"].get("SE_LogMessage", "cdecl")
    SE_LogMessage.argtypes = [String]
    SE_LogMessage.restype = None

    ctypes_SE_LogMessage = SE_LogMessage
    def SE_LogMessage(message : String) -> None : 
        return ctypes_SE_LogMessage(message)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1230
if _libs["esminiLib"].has("SE_ViewerShowFeature", "cdecl"):
    SE_ViewerShowFeature = _libs["esminiLib"].get("SE_ViewerShowFeature", "cdecl")
    SE_ViewerShowFeature.argtypes = [c_int, c_bool]
    SE_ViewerShowFeature.restype = None

    ctypes_SE_ViewerShowFeature = SE_ViewerShowFeature
    def SE_ViewerShowFeature(featureType : c_int, enable : c_bool) -> None : 
        return ctypes_SE_ViewerShowFeature(featureType, enable)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1242
if _libs["esminiLib"].has("SE_SimpleVehicleCreate", "cdecl"):
    SE_SimpleVehicleCreate = _libs["esminiLib"].get("SE_SimpleVehicleCreate", "cdecl")
    SE_SimpleVehicleCreate.argtypes = [c_float, c_float, c_float, c_float, c_float]
    SE_SimpleVehicleCreate.restype = POINTER(c_ubyte)
    SE_SimpleVehicleCreate.errcheck = lambda v,*a : cast(v, c_void_p)

    ctypes_SE_SimpleVehicleCreate = SE_SimpleVehicleCreate
    def SE_SimpleVehicleCreate(x : c_float, y : c_float, h : c_float, length : c_float, speed : c_float) -> POINTER(c_ubyte) : 
        return ctypes_SE_SimpleVehicleCreate(x, y, h, length, speed)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1247
if _libs["esminiLib"].has("SE_SimpleVehicleDelete", "cdecl"):
    SE_SimpleVehicleDelete = _libs["esminiLib"].get("SE_SimpleVehicleDelete", "cdecl")
    SE_SimpleVehicleDelete.argtypes = [POINTER(None)]
    SE_SimpleVehicleDelete.restype = None

    ctypes_SE_SimpleVehicleDelete = SE_SimpleVehicleDelete
    def SE_SimpleVehicleDelete(handleSimpleVehicle : POINTER(None)) -> None : 
        return ctypes_SE_SimpleVehicleDelete(handleSimpleVehicle)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1256
if _libs["esminiLib"].has("SE_SimpleVehicleControlBinary", "cdecl"):
    SE_SimpleVehicleControlBinary = _libs["esminiLib"].get("SE_SimpleVehicleControlBinary", "cdecl")
    SE_SimpleVehicleControlBinary.argtypes = [POINTER(None), c_double, c_int, c_int]
    SE_SimpleVehicleControlBinary.restype = None

    ctypes_SE_SimpleVehicleControlBinary = SE_SimpleVehicleControlBinary
    def SE_SimpleVehicleControlBinary(handleSimpleVehicle : POINTER(None), dt : c_double, throttle : c_int, steering : c_int) -> None : 
        return ctypes_SE_SimpleVehicleControlBinary(handleSimpleVehicle, dt, throttle, steering)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1268
if _libs["esminiLib"].has("SE_SimpleVehicleControlAnalog", "cdecl"):
    SE_SimpleVehicleControlAnalog = _libs["esminiLib"].get("SE_SimpleVehicleControlAnalog", "cdecl")
    SE_SimpleVehicleControlAnalog.argtypes = [POINTER(None), c_double, c_double, c_double]
    SE_SimpleVehicleControlAnalog.restype = None

    ctypes_SE_SimpleVehicleControlAnalog = SE_SimpleVehicleControlAnalog
    def SE_SimpleVehicleControlAnalog(handleSimpleVehicle : POINTER(None), dt : c_double, throttle : c_double, steering : c_double) -> None : 
        return ctypes_SE_SimpleVehicleControlAnalog(handleSimpleVehicle, dt, throttle, steering)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1280
if _libs["esminiLib"].has("SE_SimpleVehicleControlTarget", "cdecl"):
    SE_SimpleVehicleControlTarget = _libs["esminiLib"].get("SE_SimpleVehicleControlTarget", "cdecl")
    SE_SimpleVehicleControlTarget.argtypes = [POINTER(None), c_double, c_double, c_double]
    SE_SimpleVehicleControlTarget.restype = None

    ctypes_SE_SimpleVehicleControlTarget = SE_SimpleVehicleControlTarget
    def SE_SimpleVehicleControlTarget(handleSimpleVehicle : POINTER(None), dt : c_double, target_speed : c_double, heading_to_target : c_double) -> None : 
        return ctypes_SE_SimpleVehicleControlTarget(handleSimpleVehicle, dt, target_speed, heading_to_target)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1286
if _libs["esminiLib"].has("SE_SimpleVehicleSetMaxSpeed", "cdecl"):
    SE_SimpleVehicleSetMaxSpeed = _libs["esminiLib"].get("SE_SimpleVehicleSetMaxSpeed", "cdecl")
    SE_SimpleVehicleSetMaxSpeed.argtypes = [POINTER(None), c_float]
    SE_SimpleVehicleSetMaxSpeed.restype = None

    ctypes_SE_SimpleVehicleSetMaxSpeed = SE_SimpleVehicleSetMaxSpeed
    def SE_SimpleVehicleSetMaxSpeed(handleSimpleVehicle : POINTER(None), speed : c_float) -> None : 
        return ctypes_SE_SimpleVehicleSetMaxSpeed(handleSimpleVehicle, speed)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1292
if _libs["esminiLib"].has("SE_SimpleVehicleSetMaxAcceleration", "cdecl"):
    SE_SimpleVehicleSetMaxAcceleration = _libs["esminiLib"].get("SE_SimpleVehicleSetMaxAcceleration", "cdecl")
    SE_SimpleVehicleSetMaxAcceleration.argtypes = [POINTER(None), c_float]
    SE_SimpleVehicleSetMaxAcceleration.restype = None

    ctypes_SE_SimpleVehicleSetMaxAcceleration = SE_SimpleVehicleSetMaxAcceleration
    def SE_SimpleVehicleSetMaxAcceleration(handleSimpleVehicle : POINTER(None), maxAcceleration : c_float) -> None : 
        return ctypes_SE_SimpleVehicleSetMaxAcceleration(handleSimpleVehicle, maxAcceleration)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1298
if _libs["esminiLib"].has("SE_SimpleVehicleSetMaxDeceleration", "cdecl"):
    SE_SimpleVehicleSetMaxDeceleration = _libs["esminiLib"].get("SE_SimpleVehicleSetMaxDeceleration", "cdecl")
    SE_SimpleVehicleSetMaxDeceleration.argtypes = [POINTER(None), c_float]
    SE_SimpleVehicleSetMaxDeceleration.restype = None

    ctypes_SE_SimpleVehicleSetMaxDeceleration = SE_SimpleVehicleSetMaxDeceleration
    def SE_SimpleVehicleSetMaxDeceleration(handleSimpleVehicle : POINTER(None), maxDeceleration : c_float) -> None : 
        return ctypes_SE_SimpleVehicleSetMaxDeceleration(handleSimpleVehicle, maxDeceleration)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1304
if _libs["esminiLib"].has("SE_SimpleVehicleSetEngineBrakeFactor", "cdecl"):
    SE_SimpleVehicleSetEngineBrakeFactor = _libs["esminiLib"].get("SE_SimpleVehicleSetEngineBrakeFactor", "cdecl")
    SE_SimpleVehicleSetEngineBrakeFactor.argtypes = [POINTER(None), c_float]
    SE_SimpleVehicleSetEngineBrakeFactor.restype = None

    ctypes_SE_SimpleVehicleSetEngineBrakeFactor = SE_SimpleVehicleSetEngineBrakeFactor
    def SE_SimpleVehicleSetEngineBrakeFactor(handleSimpleVehicle : POINTER(None), engineBrakeFactor : c_float) -> None : 
        return ctypes_SE_SimpleVehicleSetEngineBrakeFactor(handleSimpleVehicle, engineBrakeFactor)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1310
if _libs["esminiLib"].has("SE_SimpleVehicleSteeringScale", "cdecl"):
    SE_SimpleVehicleSteeringScale = _libs["esminiLib"].get("SE_SimpleVehicleSteeringScale", "cdecl")
    SE_SimpleVehicleSteeringScale.argtypes = [POINTER(None), c_float]
    SE_SimpleVehicleSteeringScale.restype = None

    ctypes_SE_SimpleVehicleSteeringScale = SE_SimpleVehicleSteeringScale
    def SE_SimpleVehicleSteeringScale(handleSimpleVehicle : POINTER(None), steeringScale : c_float) -> None : 
        return ctypes_SE_SimpleVehicleSteeringScale(handleSimpleVehicle, steeringScale)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1316
if _libs["esminiLib"].has("SE_SimpleVehicleSteeringReturnFactor", "cdecl"):
    SE_SimpleVehicleSteeringReturnFactor = _libs["esminiLib"].get("SE_SimpleVehicleSteeringReturnFactor", "cdecl")
    SE_SimpleVehicleSteeringReturnFactor.argtypes = [POINTER(None), c_float]
    SE_SimpleVehicleSteeringReturnFactor.restype = None

    ctypes_SE_SimpleVehicleSteeringReturnFactor = SE_SimpleVehicleSteeringReturnFactor
    def SE_SimpleVehicleSteeringReturnFactor(handleSimpleVehicle : POINTER(None), steeringReturnFactor : c_float) -> None : 
        return ctypes_SE_SimpleVehicleSteeringReturnFactor(handleSimpleVehicle, steeringReturnFactor)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1322
if _libs["esminiLib"].has("SE_SimpleVehicleSteeringRate", "cdecl"):
    SE_SimpleVehicleSteeringRate = _libs["esminiLib"].get("SE_SimpleVehicleSteeringRate", "cdecl")
    SE_SimpleVehicleSteeringRate.argtypes = [POINTER(None), c_float]
    SE_SimpleVehicleSteeringRate.restype = None

    ctypes_SE_SimpleVehicleSteeringRate = SE_SimpleVehicleSteeringRate
    def SE_SimpleVehicleSteeringRate(handleSimpleVehicle : POINTER(None), steeringRate : c_float) -> None : 
        return ctypes_SE_SimpleVehicleSteeringRate(handleSimpleVehicle, steeringRate)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1328
if _libs["esminiLib"].has("SE_SimpleVehicleGetState", "cdecl"):
    SE_SimpleVehicleGetState = _libs["esminiLib"].get("SE_SimpleVehicleGetState", "cdecl")
    SE_SimpleVehicleGetState.argtypes = [POINTER(None), POINTER(SE_SimpleVehicleState)]
    SE_SimpleVehicleGetState.restype = None

    ctypes_SE_SimpleVehicleGetState = SE_SimpleVehicleGetState
    def SE_SimpleVehicleGetState(handleSimpleVehicle : POINTER(None), state : POINTER(SE_SimpleVehicleState)) -> None : 
        return ctypes_SE_SimpleVehicleGetState(handleSimpleVehicle, state)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1335
if _libs["esminiLib"].has("SE_SetOffScreenRendering", "cdecl"):
    SE_SetOffScreenRendering = _libs["esminiLib"].get("SE_SetOffScreenRendering", "cdecl")
    SE_SetOffScreenRendering.argtypes = [c_bool]
    SE_SetOffScreenRendering.restype = c_int

    ctypes_SE_SetOffScreenRendering = SE_SetOffScreenRendering
    def SE_SetOffScreenRendering(state : c_bool) -> c_int : 
        return ctypes_SE_SetOffScreenRendering(state)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1342
if _libs["esminiLib"].has("SE_SaveImagesToRAM", "cdecl"):
    SE_SaveImagesToRAM = _libs["esminiLib"].get("SE_SaveImagesToRAM", "cdecl")
    SE_SaveImagesToRAM.argtypes = [c_bool]
    SE_SaveImagesToRAM.restype = c_int

    ctypes_SE_SaveImagesToRAM = SE_SaveImagesToRAM
    def SE_SaveImagesToRAM(state : c_bool) -> c_int : 
        return ctypes_SE_SaveImagesToRAM(state)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1349
if _libs["esminiLib"].has("SE_SaveImagesToFile", "cdecl"):
    SE_SaveImagesToFile = _libs["esminiLib"].get("SE_SaveImagesToFile", "cdecl")
    SE_SaveImagesToFile.argtypes = [c_int]
    SE_SaveImagesToFile.restype = c_int

    ctypes_SE_SaveImagesToFile = SE_SaveImagesToFile
    def SE_SaveImagesToFile(nrOfFrames : c_int) -> c_int : 
        return ctypes_SE_SaveImagesToFile(nrOfFrames)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1356
if _libs["esminiLib"].has("SE_FetchImage", "cdecl"):
    SE_FetchImage = _libs["esminiLib"].get("SE_FetchImage", "cdecl")
    SE_FetchImage.argtypes = [POINTER(SE_Image)]
    SE_FetchImage.restype = c_int

    ctypes_SE_FetchImage = SE_FetchImage
    def SE_FetchImage(image : POINTER(SE_Image)) -> c_int : 
        return ctypes_SE_FetchImage(image)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1366
if _libs["esminiLib"].has("SE_RegisterImageCallback", "cdecl"):
    SE_RegisterImageCallback = _libs["esminiLib"].get("SE_RegisterImageCallback", "cdecl")
    SE_RegisterImageCallback.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(SE_Image), POINTER(None)), POINTER(None)]
    SE_RegisterImageCallback.restype = None

    ctypes_SE_RegisterImageCallback = SE_RegisterImageCallback
    def SE_RegisterImageCallback(fun_1 : CFUNCTYPE(UNCHECKED(None), POINTER(SE_Image), POINTER(None)), user_data : POINTER(None)) -> None : 
        return ctypes_SE_RegisterImageCallback(fun_1, user_data)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1380
if _libs["esminiLib"].has("SE_WritePPMImage", "cdecl"):
    SE_WritePPMImage = _libs["esminiLib"].get("SE_WritePPMImage", "cdecl")
    SE_WritePPMImage.argtypes = [String, c_int, c_int, POINTER(c_ubyte), c_int, c_int, c_bool]
    SE_WritePPMImage.restype = c_int

    ctypes_SE_WritePPMImage = SE_WritePPMImage
    def SE_WritePPMImage(filename : String, width : c_int, height : c_int, data : POINTER(c_ubyte), pixelSize : c_int, pixelFormat : c_int, upsidedown : c_bool) -> c_int : 
        return ctypes_SE_WritePPMImage(filename, width, height, data, pixelSize, pixelFormat, upsidedown)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1395
if _libs["esminiLib"].has("SE_WriteTGAImage", "cdecl"):
    SE_WriteTGAImage = _libs["esminiLib"].get("SE_WriteTGAImage", "cdecl")
    SE_WriteTGAImage.argtypes = [String, c_int, c_int, POINTER(c_ubyte), c_int, c_int, c_bool]
    SE_WriteTGAImage.restype = c_int

    ctypes_SE_WriteTGAImage = SE_WriteTGAImage
    def SE_WriteTGAImage(filename : String, width : c_int, height : c_int, data : POINTER(c_ubyte), pixelSize : c_int, pixelFormat : c_int, upsidedown : c_bool) -> c_int : 
        return ctypes_SE_WriteTGAImage(filename, width, height, data, pixelSize, pixelFormat, upsidedown)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1406
if _libs["esminiLib"].has("SE_AddCustomCamera", "cdecl"):
    SE_AddCustomCamera = _libs["esminiLib"].get("SE_AddCustomCamera", "cdecl")
    SE_AddCustomCamera.argtypes = [c_double, c_double, c_double, c_double, c_double]
    SE_AddCustomCamera.restype = c_int

    ctypes_SE_AddCustomCamera = SE_AddCustomCamera
    def SE_AddCustomCamera(x : c_double, y : c_double, z : c_double, h : c_double, p : c_double) -> c_int : 
        return ctypes_SE_AddCustomCamera(x, y, z, h, p)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1417
if _libs["esminiLib"].has("SE_AddCustomFixedCamera", "cdecl"):
    SE_AddCustomFixedCamera = _libs["esminiLib"].get("SE_AddCustomFixedCamera", "cdecl")
    SE_AddCustomFixedCamera.argtypes = [c_double, c_double, c_double, c_double, c_double]
    SE_AddCustomFixedCamera.restype = c_int

    ctypes_SE_AddCustomFixedCamera = SE_AddCustomFixedCamera
    def SE_AddCustomFixedCamera(x : c_double, y : c_double, z : c_double, h : c_double, p : c_double) -> c_int : 
        return ctypes_SE_AddCustomFixedCamera(x, y, z, h, p)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1426
if _libs["esminiLib"].has("SE_AddCustomAimingCamera", "cdecl"):
    SE_AddCustomAimingCamera = _libs["esminiLib"].get("SE_AddCustomAimingCamera", "cdecl")
    SE_AddCustomAimingCamera.argtypes = [c_double, c_double, c_double]
    SE_AddCustomAimingCamera.restype = c_int

    ctypes_SE_AddCustomAimingCamera = SE_AddCustomAimingCamera
    def SE_AddCustomAimingCamera(x : c_double, y : c_double, z : c_double) -> c_int : 
        return ctypes_SE_AddCustomAimingCamera(x, y, z)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1436
if _libs["esminiLib"].has("SE_AddCustomFixedAimingCamera", "cdecl"):
    SE_AddCustomFixedAimingCamera = _libs["esminiLib"].get("SE_AddCustomFixedAimingCamera", "cdecl")
    SE_AddCustomFixedAimingCamera.argtypes = [c_double, c_double, c_double]
    SE_AddCustomFixedAimingCamera.restype = c_int

    ctypes_SE_AddCustomFixedAimingCamera = SE_AddCustomFixedAimingCamera
    def SE_AddCustomFixedAimingCamera(x : c_double, y : c_double, z : c_double) -> c_int : 
        return ctypes_SE_AddCustomFixedAimingCamera(x, y, z)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1446
if _libs["esminiLib"].has("SE_AddCustomFixedTopCamera", "cdecl"):
    SE_AddCustomFixedTopCamera = _libs["esminiLib"].get("SE_AddCustomFixedTopCamera", "cdecl")
    SE_AddCustomFixedTopCamera.argtypes = [c_double, c_double, c_double, c_double]
    SE_AddCustomFixedTopCamera.restype = c_int

    ctypes_SE_AddCustomFixedTopCamera = SE_AddCustomFixedTopCamera
    def SE_AddCustomFixedTopCamera(x : c_double, y : c_double, z : c_double, rot : c_double) -> c_int : 
        return ctypes_SE_AddCustomFixedTopCamera(x, y, z, rot)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1453
if _libs["esminiLib"].has("SE_SetCameraMode", "cdecl"):
    SE_SetCameraMode = _libs["esminiLib"].get("SE_SetCameraMode", "cdecl")
    SE_SetCameraMode.argtypes = [c_int]
    SE_SetCameraMode.restype = c_int

    ctypes_SE_SetCameraMode = SE_SetCameraMode
    def SE_SetCameraMode(mode : c_int) -> c_int : 
        return ctypes_SE_SetCameraMode(mode)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1460
if _libs["esminiLib"].has("SE_SetCameraObjectFocus", "cdecl"):
    SE_SetCameraObjectFocus = _libs["esminiLib"].get("SE_SetCameraObjectFocus", "cdecl")
    SE_SetCameraObjectFocus.argtypes = [c_int]
    SE_SetCameraObjectFocus.restype = c_int

    ctypes_SE_SetCameraObjectFocus = SE_SetCameraObjectFocus
    def SE_SetCameraObjectFocus(object_id : c_int) -> c_int : 
        return ctypes_SE_SetCameraObjectFocus(object_id)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1467
if _libs["esminiLib"].has("SE_GetNumberOfRoutePoints", "cdecl"):
    SE_GetNumberOfRoutePoints = _libs["esminiLib"].get("SE_GetNumberOfRoutePoints", "cdecl")
    SE_GetNumberOfRoutePoints.argtypes = [c_int]
    SE_GetNumberOfRoutePoints.restype = c_int

    ctypes_SE_GetNumberOfRoutePoints = SE_GetNumberOfRoutePoints
    def SE_GetNumberOfRoutePoints(object_id : c_int) -> c_int : 
        return ctypes_SE_GetNumberOfRoutePoints(object_id)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 1475
if _libs["esminiLib"].has("SE_GetRoutePoint", "cdecl"):
    SE_GetRoutePoint = _libs["esminiLib"].get("SE_GetRoutePoint", "cdecl")
    SE_GetRoutePoint.argtypes = [c_int, c_int, POINTER(SE_RouteInfo)]
    SE_GetRoutePoint.restype = c_int

    ctypes_SE_GetRoutePoint = SE_GetRoutePoint
    def SE_GetRoutePoint(object_id : c_int, route_index : c_int, routeinfo : POINTER(SE_RouteInfo)) -> c_int : 
        return ctypes_SE_GetRoutePoint(object_id, route_index, routeinfo)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiLib.hpp: 21
try:
    SE_PARAM_NAME_SIZE = 32
except:
    pass

# No inserted files

# No prefix-stripping

