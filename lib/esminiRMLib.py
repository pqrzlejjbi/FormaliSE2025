r"""Wrapper for esminiRMLib.hpp

Generated with:
/usr/local/bin/ctypesgen --include-stdbool -L ./ --library=esminiRMLib ./esminiRMLib.hpp -o ./esminiRMLib.py

Do not modify this file.
"""
from __future__ import annotations

__docformat__ = "restructuredtext"

# Begin preamble for Python

from typing import TypeVar, Type, get_type_hints
import ctypes
import sys
from ctypes import *  # noqa: F401, F403

T = TypeVar("T")

def struct_decorator(cls: Type[T]) -> Type[T]:
    class Internal(cls.__base__):
        __annotations__ = cls.__annotations__
        __slots__ = list(cls.__annotations__.keys())
    return Internal

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
_libs["esminiRMLib"] = load_library("esminiRMLib")

# 1 libraries
# End libraries

# No modules

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 26
@struct_decorator
class struct_anon_1(Structure):
    x : c_float
    y : c_float
    z : c_float

struct_anon_1._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('z', c_float),
]

RM_PositionXYZ = struct_anon_1# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 26

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 42
@struct_decorator
class struct_anon_2(Structure):
    x : c_float
    y : c_float
    z : c_float
    h : c_float
    p : c_float
    r : c_float
    hRelative : c_float
    roadId : c_int
    junctionId : c_int
    laneId : c_int
    laneOffset : c_float
    s : c_float

struct_anon_2._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('z', c_float),
    ('h', c_float),
    ('p', c_float),
    ('r', c_float),
    ('hRelative', c_float),
    ('roadId', c_int),
    ('junctionId', c_int),
    ('laneId', c_int),
    ('laneOffset', c_float),
    ('s', c_float),
]

RM_PositionData = struct_anon_2# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 42

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 59
@struct_decorator
class struct_anon_3(Structure):
    pos : RM_PositionXYZ
    heading : c_float
    pitch : c_float
    roll : c_float
    width : c_float
    curvature : c_float
    speed_limit : c_float
    roadId : c_int
    junctionId : c_int
    laneId : c_int
    laneOffset : c_float
    s : c_float
    t : c_float

struct_anon_3._fields_ = [
    ('pos', RM_PositionXYZ),
    ('heading', c_float),
    ('pitch', c_float),
    ('roll', c_float),
    ('width', c_float),
    ('curvature', c_float),
    ('speed_limit', c_float),
    ('roadId', c_int),
    ('junctionId', c_int),
    ('laneId', c_int),
    ('laneOffset', c_float),
    ('s', c_float),
    ('t', c_float),
]

RM_RoadLaneInfo = struct_anon_3# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 59

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 66
@struct_decorator
class struct_anon_4(Structure):
    road_lane_info : RM_RoadLaneInfo
    relative_pos : RM_PositionXYZ
    relative_h : c_float

struct_anon_4._fields_ = [
    ('road_lane_info', RM_RoadLaneInfo),
    ('relative_pos', RM_PositionXYZ),
    ('relative_h', c_float),
]

RM_RoadProbeInfo = struct_anon_4# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 66

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 73
@struct_decorator
class struct_anon_5(Structure):
    ds : c_float
    dt : c_float
    dLaneId : c_int

struct_anon_5._fields_ = [
    ('ds', c_float),
    ('dt', c_float),
    ('dLaneId', c_int),
]

RM_PositionDiff = struct_anon_5# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 73

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 91
@struct_decorator
class struct_anon_6(Structure):
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

struct_anon_6._fields_ = [
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

RM_RoadSign = struct_anon_6# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 91

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 97
@struct_decorator
class struct_anon_7(Structure):
    fromLane : c_int
    toLane : c_int

struct_anon_7._fields_ = [
    ('fromLane', c_int),
    ('toLane', c_int),
]

RM_RoadObjValidity = struct_anon_7# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 97

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 121
@struct_decorator
class struct_anon_8(Structure):
    a_ : c_float
    axis_ : String
    b_ : c_float
    ellps_ : String
    k_ : c_float
    k_0_ : c_float
    lat_0_ : c_float
    lon_0_ : c_float
    lon_wrap_ : c_float
    over_ : c_float
    pm_ : String
    proj_ : String
    units_ : String
    vunits_ : String
    x_0_ : c_float
    y_0_ : c_float
    datum_ : String
    geo_id_grids_ : String
    zone_ : c_float
    towgs84_ : c_int

struct_anon_8._fields_ = [
    ('a_', c_float),
    ('axis_', String),
    ('b_', c_float),
    ('ellps_', String),
    ('k_', c_float),
    ('k_0_', c_float),
    ('lat_0_', c_float),
    ('lon_0_', c_float),
    ('lon_wrap_', c_float),
    ('over_', c_float),
    ('pm_', String),
    ('proj_', String),
    ('units_', String),
    ('vunits_', String),
    ('x_0_', c_float),
    ('y_0_', c_float),
    ('datum_', String),
    ('geo_id_grids_', String),
    ('zone_', c_float),
    ('towgs84_', c_int),
]

RM_GeoReference = struct_anon_8# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 121

# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 128
if _libs["esminiRMLib"].has("RM_Init", "cdecl"):
    RM_Init = _libs["esminiRMLib"].get("RM_Init", "cdecl")
    RM_Init.argtypes = [String]
    RM_Init.restype = c_int

    ctypes_RM_Init = RM_Init
    def RM_Init(odrFilename : String) -> c_int : 
        return ctypes_RM_Init(odrFilename)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 130
if _libs["esminiRMLib"].has("RM_Close", "cdecl"):
    RM_Close = _libs["esminiRMLib"].get("RM_Close", "cdecl")
    RM_Close.argtypes = []
    RM_Close.restype = c_int

    ctypes_RM_Close = RM_Close
    def RM_Close() -> c_int : 
        return ctypes_RM_Close()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 139
if _libs["esminiRMLib"].has("RM_SetLogFilePath", "cdecl"):
    RM_SetLogFilePath = _libs["esminiRMLib"].get("RM_SetLogFilePath", "cdecl")
    RM_SetLogFilePath.argtypes = [String]
    RM_SetLogFilePath.restype = None

    ctypes_RM_SetLogFilePath = RM_SetLogFilePath
    def RM_SetLogFilePath(logFilePath : String) -> None : 
        return ctypes_RM_SetLogFilePath(logFilePath)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 145
if _libs["esminiRMLib"].has("RM_CreatePosition", "cdecl"):
    RM_CreatePosition = _libs["esminiRMLib"].get("RM_CreatePosition", "cdecl")
    RM_CreatePosition.argtypes = []
    RM_CreatePosition.restype = c_int

    ctypes_RM_CreatePosition = RM_CreatePosition
    def RM_CreatePosition() -> c_int : 
        return ctypes_RM_CreatePosition()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 151
if _libs["esminiRMLib"].has("RM_GetNrOfPositions", "cdecl"):
    RM_GetNrOfPositions = _libs["esminiRMLib"].get("RM_GetNrOfPositions", "cdecl")
    RM_GetNrOfPositions.argtypes = []
    RM_GetNrOfPositions.restype = c_int

    ctypes_RM_GetNrOfPositions = RM_GetNrOfPositions
    def RM_GetNrOfPositions() -> c_int : 
        return ctypes_RM_GetNrOfPositions()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 158
if _libs["esminiRMLib"].has("RM_DeletePosition", "cdecl"):
    RM_DeletePosition = _libs["esminiRMLib"].get("RM_DeletePosition", "cdecl")
    RM_DeletePosition.argtypes = [c_int]
    RM_DeletePosition.restype = c_int

    ctypes_RM_DeletePosition = RM_DeletePosition
    def RM_DeletePosition(handle : c_int) -> c_int : 
        return ctypes_RM_DeletePosition(handle)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 165
if _libs["esminiRMLib"].has("RM_CopyPosition", "cdecl"):
    RM_CopyPosition = _libs["esminiRMLib"].get("RM_CopyPosition", "cdecl")
    RM_CopyPosition.argtypes = [c_int]
    RM_CopyPosition.restype = c_int

    ctypes_RM_CopyPosition = RM_CopyPosition
    def RM_CopyPosition(handle : c_int) -> c_int : 
        return ctypes_RM_CopyPosition(handle)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 176
if _libs["esminiRMLib"].has("RM_SetAlignMode", "cdecl"):
    RM_SetAlignMode = _libs["esminiRMLib"].get("RM_SetAlignMode", "cdecl")
    RM_SetAlignMode.argtypes = [c_int, c_int]
    RM_SetAlignMode.restype = None

    ctypes_RM_SetAlignMode = RM_SetAlignMode
    def RM_SetAlignMode(handle : c_int, mode : c_int) -> None : 
        return ctypes_RM_SetAlignMode(handle, mode)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 187
if _libs["esminiRMLib"].has("RM_SetAlignModeH", "cdecl"):
    RM_SetAlignModeH = _libs["esminiRMLib"].get("RM_SetAlignModeH", "cdecl")
    RM_SetAlignModeH.argtypes = [c_int, c_int]
    RM_SetAlignModeH.restype = None

    ctypes_RM_SetAlignModeH = RM_SetAlignModeH
    def RM_SetAlignModeH(handle : c_int, mode : c_int) -> None : 
        return ctypes_RM_SetAlignModeH(handle, mode)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 198
if _libs["esminiRMLib"].has("RM_SetAlignModeP", "cdecl"):
    RM_SetAlignModeP = _libs["esminiRMLib"].get("RM_SetAlignModeP", "cdecl")
    RM_SetAlignModeP.argtypes = [c_int, c_int]
    RM_SetAlignModeP.restype = None

    ctypes_RM_SetAlignModeP = RM_SetAlignModeP
    def RM_SetAlignModeP(handle : c_int, mode : c_int) -> None : 
        return ctypes_RM_SetAlignModeP(handle, mode)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 209
if _libs["esminiRMLib"].has("RM_SetAlignModeR", "cdecl"):
    RM_SetAlignModeR = _libs["esminiRMLib"].get("RM_SetAlignModeR", "cdecl")
    RM_SetAlignModeR.argtypes = [c_int, c_int]
    RM_SetAlignModeR.restype = None

    ctypes_RM_SetAlignModeR = RM_SetAlignModeR
    def RM_SetAlignModeR(handle : c_int, mode : c_int) -> None : 
        return ctypes_RM_SetAlignModeR(handle, mode)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 220
if _libs["esminiRMLib"].has("RM_SetAlignModeZ", "cdecl"):
    RM_SetAlignModeZ = _libs["esminiRMLib"].get("RM_SetAlignModeZ", "cdecl")
    RM_SetAlignModeZ.argtypes = [c_int, c_int]
    RM_SetAlignModeZ.restype = None

    ctypes_RM_SetAlignModeZ = RM_SetAlignModeZ
    def RM_SetAlignModeZ(handle : c_int, mode : c_int) -> None : 
        return ctypes_RM_SetAlignModeZ(handle, mode)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 227
if _libs["esminiRMLib"].has("RM_SetLockOnLane", "cdecl"):
    RM_SetLockOnLane = _libs["esminiRMLib"].get("RM_SetLockOnLane", "cdecl")
    RM_SetLockOnLane.argtypes = [c_int, c_bool]
    RM_SetLockOnLane.restype = c_int

    ctypes_RM_SetLockOnLane = RM_SetLockOnLane
    def RM_SetLockOnLane(handle : c_int, mode : c_bool) -> c_int : 
        return ctypes_RM_SetLockOnLane(handle, mode)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 233
if _libs["esminiRMLib"].has("RM_GetNumberOfRoads", "cdecl"):
    RM_GetNumberOfRoads = _libs["esminiRMLib"].get("RM_GetNumberOfRoads", "cdecl")
    RM_GetNumberOfRoads.argtypes = []
    RM_GetNumberOfRoads.restype = c_int

    ctypes_RM_GetNumberOfRoads = RM_GetNumberOfRoads
    def RM_GetNumberOfRoads() -> c_int : 
        return ctypes_RM_GetNumberOfRoads()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 242
if _libs["esminiRMLib"].has("RM_GetSpeedUnit", "cdecl"):
    RM_GetSpeedUnit = _libs["esminiRMLib"].get("RM_GetSpeedUnit", "cdecl")
    RM_GetSpeedUnit.argtypes = []
    RM_GetSpeedUnit.restype = c_int

    ctypes_RM_GetSpeedUnit = RM_GetSpeedUnit
    def RM_GetSpeedUnit() -> c_int : 
        return ctypes_RM_GetSpeedUnit()


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 249
if _libs["esminiRMLib"].has("RM_GetIdOfRoadFromIndex", "cdecl"):
    RM_GetIdOfRoadFromIndex = _libs["esminiRMLib"].get("RM_GetIdOfRoadFromIndex", "cdecl")
    RM_GetIdOfRoadFromIndex.argtypes = [c_int]
    RM_GetIdOfRoadFromIndex.restype = c_int

    ctypes_RM_GetIdOfRoadFromIndex = RM_GetIdOfRoadFromIndex
    def RM_GetIdOfRoadFromIndex(index : c_int) -> c_int : 
        return ctypes_RM_GetIdOfRoadFromIndex(index)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 256
if _libs["esminiRMLib"].has("RM_GetRoadLength", "cdecl"):
    RM_GetRoadLength = _libs["esminiRMLib"].get("RM_GetRoadLength", "cdecl")
    RM_GetRoadLength.argtypes = [c_int]
    RM_GetRoadLength.restype = c_float

    ctypes_RM_GetRoadLength = RM_GetRoadLength
    def RM_GetRoadLength(id : c_int) -> c_float : 
        return ctypes_RM_GetRoadLength(id)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 264
if _libs["esminiRMLib"].has("RM_GetRoadNumberOfLanes", "cdecl"):
    RM_GetRoadNumberOfLanes = _libs["esminiRMLib"].get("RM_GetRoadNumberOfLanes", "cdecl")
    RM_GetRoadNumberOfLanes.argtypes = [c_int, c_float]
    RM_GetRoadNumberOfLanes.restype = c_int

    ctypes_RM_GetRoadNumberOfLanes = RM_GetRoadNumberOfLanes
    def RM_GetRoadNumberOfLanes(roadId : c_int, s : c_float) -> c_int : 
        return ctypes_RM_GetRoadNumberOfLanes(roadId, s)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 271
if _libs["esminiRMLib"].has("RM_GetNumberOfRoadsOverlapping", "cdecl"):
    RM_GetNumberOfRoadsOverlapping = _libs["esminiRMLib"].get("RM_GetNumberOfRoadsOverlapping", "cdecl")
    RM_GetNumberOfRoadsOverlapping.argtypes = [c_int]
    RM_GetNumberOfRoadsOverlapping.restype = c_int

    ctypes_RM_GetNumberOfRoadsOverlapping = RM_GetNumberOfRoadsOverlapping
    def RM_GetNumberOfRoadsOverlapping(handle : c_int) -> c_int : 
        return ctypes_RM_GetNumberOfRoadsOverlapping(handle)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 279
if _libs["esminiRMLib"].has("RM_GetOverlappingRoadId", "cdecl"):
    RM_GetOverlappingRoadId = _libs["esminiRMLib"].get("RM_GetOverlappingRoadId", "cdecl")
    RM_GetOverlappingRoadId.argtypes = [c_int, c_int]
    RM_GetOverlappingRoadId.restype = c_int

    ctypes_RM_GetOverlappingRoadId = RM_GetOverlappingRoadId
    def RM_GetOverlappingRoadId(handle : c_int, index : c_int) -> c_int : 
        return ctypes_RM_GetOverlappingRoadId(handle, index)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 288
if _libs["esminiRMLib"].has("RM_GetLaneIdByIndex", "cdecl"):
    RM_GetLaneIdByIndex = _libs["esminiRMLib"].get("RM_GetLaneIdByIndex", "cdecl")
    RM_GetLaneIdByIndex.argtypes = [c_int, c_int, c_float]
    RM_GetLaneIdByIndex.restype = c_int

    ctypes_RM_GetLaneIdByIndex = RM_GetLaneIdByIndex
    def RM_GetLaneIdByIndex(roadId : c_int, laneIndex : c_int, s : c_float) -> c_int : 
        return ctypes_RM_GetLaneIdByIndex(roadId, laneIndex, s)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 300
if _libs["esminiRMLib"].has("RM_SetLanePosition", "cdecl"):
    RM_SetLanePosition = _libs["esminiRMLib"].get("RM_SetLanePosition", "cdecl")
    RM_SetLanePosition.argtypes = [c_int, c_int, c_int, c_float, c_float, c_bool]
    RM_SetLanePosition.restype = c_int

    ctypes_RM_SetLanePosition = RM_SetLanePosition
    def RM_SetLanePosition(handle : c_int, roadId : c_int, laneId : c_int, laneOffset : c_float, s : c_float, align : c_bool) -> c_int : 
        return ctypes_RM_SetLanePosition(handle, roadId, laneId, laneOffset, s, align)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 308
if _libs["esminiRMLib"].has("RM_SetS", "cdecl"):
    RM_SetS = _libs["esminiRMLib"].get("RM_SetS", "cdecl")
    RM_SetS.argtypes = [c_int, c_float]
    RM_SetS.restype = c_int

    ctypes_RM_SetS = RM_SetS
    def RM_SetS(handle : c_int, s : c_float) -> c_int : 
        return ctypes_RM_SetS(handle, s)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 321
if _libs["esminiRMLib"].has("RM_SetWorldPosition", "cdecl"):
    RM_SetWorldPosition = _libs["esminiRMLib"].get("RM_SetWorldPosition", "cdecl")
    RM_SetWorldPosition.argtypes = [c_int, c_float, c_float, c_float, c_float, c_float, c_float]
    RM_SetWorldPosition.restype = c_int

    ctypes_RM_SetWorldPosition = RM_SetWorldPosition
    def RM_SetWorldPosition(handle : c_int, x : c_float, y : c_float, z : c_float, h : c_float, p : c_float, r : c_float) -> c_int : 
        return ctypes_RM_SetWorldPosition(handle, x, y, z, h, p, r)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 331
if _libs["esminiRMLib"].has("RM_SetWorldXYHPosition", "cdecl"):
    RM_SetWorldXYHPosition = _libs["esminiRMLib"].get("RM_SetWorldXYHPosition", "cdecl")
    RM_SetWorldXYHPosition.argtypes = [c_int, c_float, c_float, c_float]
    RM_SetWorldXYHPosition.restype = c_int

    ctypes_RM_SetWorldXYHPosition = RM_SetWorldXYHPosition
    def RM_SetWorldXYHPosition(handle : c_int, x : c_float, y : c_float, h : c_float) -> c_int : 
        return ctypes_RM_SetWorldXYHPosition(handle, x, y, h)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 342
if _libs["esminiRMLib"].has("RM_SetWorldXYZHPosition", "cdecl"):
    RM_SetWorldXYZHPosition = _libs["esminiRMLib"].get("RM_SetWorldXYZHPosition", "cdecl")
    RM_SetWorldXYZHPosition.argtypes = [c_int, c_float, c_float, c_float, c_float]
    RM_SetWorldXYZHPosition.restype = c_int

    ctypes_RM_SetWorldXYZHPosition = RM_SetWorldXYZHPosition
    def RM_SetWorldXYZHPosition(handle : c_int, x : c_float, y : c_float, z : c_float, h : c_float) -> c_int : 
        return ctypes_RM_SetWorldXYZHPosition(handle, x, y, z, h)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 350
if _libs["esminiRMLib"].has("RM_SetRoadId", "cdecl"):
    RM_SetRoadId = _libs["esminiRMLib"].get("RM_SetRoadId", "cdecl")
    RM_SetRoadId.argtypes = [c_int, c_int]
    RM_SetRoadId.restype = c_int

    ctypes_RM_SetRoadId = RM_SetRoadId
    def RM_SetRoadId(handle : c_int, roadId : c_int) -> c_int : 
        return ctypes_RM_SetRoadId(handle, roadId)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 359
if _libs["esminiRMLib"].has("RM_PositionMoveForward", "cdecl"):
    RM_PositionMoveForward = _libs["esminiRMLib"].get("RM_PositionMoveForward", "cdecl")
    RM_PositionMoveForward.argtypes = [c_int, c_float, c_float]
    RM_PositionMoveForward.restype = c_int

    ctypes_RM_PositionMoveForward = RM_PositionMoveForward
    def RM_PositionMoveForward(handle : c_int, dist : c_float, junctionSelectorAngle : c_float) -> c_int : 
        return ctypes_RM_PositionMoveForward(handle, dist, junctionSelectorAngle)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 367
if _libs["esminiRMLib"].has("RM_GetPositionData", "cdecl"):
    RM_GetPositionData = _libs["esminiRMLib"].get("RM_GetPositionData", "cdecl")
    RM_GetPositionData.argtypes = [c_int, POINTER(RM_PositionData)]
    RM_GetPositionData.restype = c_int

    ctypes_RM_GetPositionData = RM_GetPositionData
    def RM_GetPositionData(handle : c_int, data : POINTER(RM_PositionData)) -> c_int : 
        return ctypes_RM_GetPositionData(handle, data)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 374
if _libs["esminiRMLib"].has("RM_GetSpeedLimit", "cdecl"):
    RM_GetSpeedLimit = _libs["esminiRMLib"].get("RM_GetSpeedLimit", "cdecl")
    RM_GetSpeedLimit.argtypes = [c_int]
    RM_GetSpeedLimit.restype = c_float

    ctypes_RM_GetSpeedLimit = RM_GetSpeedLimit
    def RM_GetSpeedLimit(handle : c_int) -> c_float : 
        return ctypes_RM_GetSpeedLimit(handle)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 386
if _libs["esminiRMLib"].has("RM_GetLaneInfo", "cdecl"):
    RM_GetLaneInfo = _libs["esminiRMLib"].get("RM_GetLaneInfo", "cdecl")
    RM_GetLaneInfo.argtypes = [c_int, c_float, POINTER(RM_RoadLaneInfo), c_int, c_bool]
    RM_GetLaneInfo.restype = c_int

    ctypes_RM_GetLaneInfo = RM_GetLaneInfo
    def RM_GetLaneInfo(handle : c_int, lookahead_distance : c_float, data : POINTER(RM_RoadLaneInfo), lookAheadMode : c_int, inRoadDrivingDirection : c_bool) -> c_int : 
        return ctypes_RM_GetLaneInfo(handle, lookahead_distance, data, lookAheadMode, inRoadDrivingDirection)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 398
if _libs["esminiRMLib"].has("RM_GetProbeInfo", "cdecl"):
    RM_GetProbeInfo = _libs["esminiRMLib"].get("RM_GetProbeInfo", "cdecl")
    RM_GetProbeInfo.argtypes = [c_int, c_float, POINTER(RM_RoadProbeInfo), c_int, c_bool]
    RM_GetProbeInfo.restype = c_int

    ctypes_RM_GetProbeInfo = RM_GetProbeInfo
    def RM_GetProbeInfo(handle : c_int, lookahead_distance : c_float, data : POINTER(RM_RoadProbeInfo), lookAheadMode : c_int, inRoadDrivingDirection : c_bool) -> c_int : 
        return ctypes_RM_GetProbeInfo(handle, lookahead_distance, data, lookAheadMode, inRoadDrivingDirection)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 406
if _libs["esminiRMLib"].has("RM_GetLaneWidth", "cdecl"):
    RM_GetLaneWidth = _libs["esminiRMLib"].get("RM_GetLaneWidth", "cdecl")
    RM_GetLaneWidth.argtypes = [c_int, c_int]
    RM_GetLaneWidth.restype = c_float

    ctypes_RM_GetLaneWidth = RM_GetLaneWidth
    def RM_GetLaneWidth(handle : c_int, lane_id : c_int) -> c_float : 
        return ctypes_RM_GetLaneWidth(handle, lane_id)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 415
if _libs["esminiRMLib"].has("RM_GetLaneWidthByRoadId", "cdecl"):
    RM_GetLaneWidthByRoadId = _libs["esminiRMLib"].get("RM_GetLaneWidthByRoadId", "cdecl")
    RM_GetLaneWidthByRoadId.argtypes = [c_int, c_int, c_float]
    RM_GetLaneWidthByRoadId.restype = c_float

    ctypes_RM_GetLaneWidthByRoadId = RM_GetLaneWidthByRoadId
    def RM_GetLaneWidthByRoadId(road_id : c_int, lane_id : c_int, s : c_float) -> c_float : 
        return ctypes_RM_GetLaneWidthByRoadId(road_id, lane_id, s)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 424
if _libs["esminiRMLib"].has("RM_GetLaneType", "cdecl"):
    RM_GetLaneType = _libs["esminiRMLib"].get("RM_GetLaneType", "cdecl")
    RM_GetLaneType.argtypes = [c_int, c_int]
    RM_GetLaneType.restype = c_int

    ctypes_RM_GetLaneType = RM_GetLaneType
    def RM_GetLaneType(handle : c_int, lane_id : c_int) -> c_int : 
        return ctypes_RM_GetLaneType(handle, lane_id)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 434
if _libs["esminiRMLib"].has("RM_GetLaneTypeByRoadId", "cdecl"):
    RM_GetLaneTypeByRoadId = _libs["esminiRMLib"].get("RM_GetLaneTypeByRoadId", "cdecl")
    RM_GetLaneTypeByRoadId.argtypes = [c_int, c_int, c_float]
    RM_GetLaneTypeByRoadId.restype = c_int

    ctypes_RM_GetLaneTypeByRoadId = RM_GetLaneTypeByRoadId
    def RM_GetLaneTypeByRoadId(road_id : c_int, lane_id : c_int, s : c_float) -> c_int : 
        return ctypes_RM_GetLaneTypeByRoadId(road_id, lane_id, s)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 443
if _libs["esminiRMLib"].has("RM_SubtractAFromB", "cdecl"):
    RM_SubtractAFromB = _libs["esminiRMLib"].get("RM_SubtractAFromB", "cdecl")
    RM_SubtractAFromB.argtypes = [c_int, c_int, POINTER(RM_PositionDiff)]
    RM_SubtractAFromB.restype = c_int

    ctypes_RM_SubtractAFromB = RM_SubtractAFromB
    def RM_SubtractAFromB(handleA : c_int, handleB : c_int, pos_diff : POINTER(RM_PositionDiff)) -> c_int : 
        return ctypes_RM_SubtractAFromB(handleA, handleB, pos_diff)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 450
if _libs["esminiRMLib"].has("RM_GetNumberOfRoadSigns", "cdecl"):
    RM_GetNumberOfRoadSigns = _libs["esminiRMLib"].get("RM_GetNumberOfRoadSigns", "cdecl")
    RM_GetNumberOfRoadSigns.argtypes = [c_int]
    RM_GetNumberOfRoadSigns.restype = c_int

    ctypes_RM_GetNumberOfRoadSigns = RM_GetNumberOfRoadSigns
    def RM_GetNumberOfRoadSigns(road_id : c_int) -> c_int : 
        return ctypes_RM_GetNumberOfRoadSigns(road_id)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 459
if _libs["esminiRMLib"].has("RM_GetRoadSign", "cdecl"):
    RM_GetRoadSign = _libs["esminiRMLib"].get("RM_GetRoadSign", "cdecl")
    RM_GetRoadSign.argtypes = [c_int, c_int, POINTER(RM_RoadSign)]
    RM_GetRoadSign.restype = c_int

    ctypes_RM_GetRoadSign = RM_GetRoadSign
    def RM_GetRoadSign(road_id : c_int, index : c_int, road_sign : POINTER(RM_RoadSign)) -> c_int : 
        return ctypes_RM_GetRoadSign(road_id, index, road_sign)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 467
if _libs["esminiRMLib"].has("RM_GetNumberOfRoadSignValidityRecords", "cdecl"):
    RM_GetNumberOfRoadSignValidityRecords = _libs["esminiRMLib"].get("RM_GetNumberOfRoadSignValidityRecords", "cdecl")
    RM_GetNumberOfRoadSignValidityRecords.argtypes = [c_int, c_int]
    RM_GetNumberOfRoadSignValidityRecords.restype = c_int

    ctypes_RM_GetNumberOfRoadSignValidityRecords = RM_GetNumberOfRoadSignValidityRecords
    def RM_GetNumberOfRoadSignValidityRecords(road_id : c_int, index : c_int) -> c_int : 
        return ctypes_RM_GetNumberOfRoadSignValidityRecords(road_id, index)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 477
if _libs["esminiRMLib"].has("RM_GetRoadSignValidityRecord", "cdecl"):
    RM_GetRoadSignValidityRecord = _libs["esminiRMLib"].get("RM_GetRoadSignValidityRecord", "cdecl")
    RM_GetRoadSignValidityRecord.argtypes = [c_int, c_int, c_int, POINTER(RM_RoadObjValidity)]
    RM_GetRoadSignValidityRecord.restype = c_int

    ctypes_RM_GetRoadSignValidityRecord = RM_GetRoadSignValidityRecord
    def RM_GetRoadSignValidityRecord(road_id : c_int, signIndex : c_int, validityIndex : c_int, validity : POINTER(RM_RoadObjValidity)) -> c_int : 
        return ctypes_RM_GetRoadSignValidityRecord(road_id, signIndex, validityIndex, validity)


# /mnt/Data/eigenes/Work/Work/AVL/MBT/MBT Code/lib/esminiRMLib.hpp: 482
if _libs["esminiRMLib"].has("RM_GetOpenDriveGeoReference", "cdecl"):
    RM_GetOpenDriveGeoReference = _libs["esminiRMLib"].get("RM_GetOpenDriveGeoReference", "cdecl")
    RM_GetOpenDriveGeoReference.argtypes = [POINTER(RM_GeoReference)]
    RM_GetOpenDriveGeoReference.restype = c_int

    ctypes_RM_GetOpenDriveGeoReference = RM_GetOpenDriveGeoReference
    def RM_GetOpenDriveGeoReference(rmGeoReference : POINTER(RM_GeoReference)) -> c_int : 
        return ctypes_RM_GetOpenDriveGeoReference(rmGeoReference)


# No inserted files

# No prefix-stripping

