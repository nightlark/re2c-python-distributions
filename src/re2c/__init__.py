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
