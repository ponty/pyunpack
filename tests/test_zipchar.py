import os
import tempfile
from os.path import dirname, join

from pyunpack import Archive

DIR = dirname(__file__)


def tmpdir():
    d = tempfile.mkdtemp(prefix="pyunpack_test_")
    return d


def ok_file(d):
    full = join(d, "测试", "test", "test.txt")
    assert os.path.exists(full)
    full = join(d, "测试", "test", "测试.txt")
    assert os.path.exists(full)


# TODO: fix test
def notest_zipchar():
    f = join(DIR, "testchar.zip")

    d = tmpdir()
    Archive(f, backend="patool").extractall(d)
    ok_file(d)

    d = tmpdir()
    Archive(f, backend="zipfile").extractall(d)
    ok_file(d)

    # d = tmpdir()
    # Archive(f).extractall(d)
    # ok_file(d)

    # d = tmpdir()
    # Archive(f, backend="auto").extractall(d)
    # ok_file(d)

    # d = tmpdir()
    # cli.extractall(f, d)
    # ok_file(d)
