import os
import tempfile
from os.path import dirname, join

from pyunpack import Archive, cli

DIR = dirname(__file__)


def ok_file(d):
    full = join(d, "cab.txt")
    assert os.path.exists(full)
    assert open(full).read() == "pyunpack cab test"


def tmpdir():
    d = tempfile.mkdtemp(prefix="pyunpack_test_")
    return d


def test_cab():
    cab = join(DIR, "test.cab")

    d = tmpdir()
    Archive(cab, backend="patool").extractall(d)
    ok_file(d)

    d = tmpdir()
    Archive(cab).extractall(d)
    ok_file(d)

    d = tmpdir()
    Archive(cab, backend="auto").extractall(d)
    ok_file(d)

    d = tmpdir()
    cli.extractall(cab, d)
    ok_file(d)
