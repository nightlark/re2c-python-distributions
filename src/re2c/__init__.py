import os
import subprocess
import sys

try:
    from ._version import __version__, __version_tuple__
except ModuleNotFoundError:
    __version__ = ""
    __version_tuple__ = ()


DATA = os.path.join(os.path.dirname(__file__), "data")
BIN_DIR = os.path.join(DATA, "bin")


def _program(name, args):
    return subprocess.call([os.path.join(BIN_DIR, name)] + args)


def re2c():
    raise SystemExit(_program("re2c", sys.argv[1:]))


def re2d():
    raise SystemExit(_program("re2d", sys.argv[1:]))


def re2go():
    raise SystemExit(_program("re2go", sys.argv[1:]))


def re2hs():
    raise SystemExit(_program("re2hs", sys.argv[1:]))


def re2java():
    raise SystemExit(_program("re2java", sys.argv[1:]))


def re2js():
    raise SystemExit(_program("re2js", sys.argv[1:]))


def re2ocaml():
    raise SystemExit(_program("re2ocaml", sys.argv[1:]))


def re2py():
    raise SystemExit(_program("re2py", sys.argv[1:]))


def re2rust():
    raise SystemExit(_program("re2rust", sys.argv[1:]))


def re2v():
    raise SystemExit(_program("re2v", sys.argv[1:]))


def re2zig():
    raise SystemExit(_program("re2zig", sys.argv[1:]))