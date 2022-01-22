import os
import tempfile
from os.path import dirname, join

from pyunpack import Archive, cli

DIR = dirname(__file__)


def ok_file(d):
    full = join(d, "rar.txt")
    assert os.path.exists(full)
    assert open(full).read() == "pyunpack rar test\n"


def tmpdir():
    d = tempfile.mkdtemp(prefix="pyunpack_test_")
    return d


def test_rar():
    f = join(DIR, "test.rar")

    d = tmpdir()
    Archive(f, backend="patool").extractall(d)
    ok_file(d)

    d = tmpdir()
    Archive(f).extractall(d)
    ok_file(d)

    d = tmpdir()
    Archive(f, backend="auto").extractall(d)
    ok_file(d)

    d = tmpdir()
    cli.extractall(f, d)
    ok_file(d)
