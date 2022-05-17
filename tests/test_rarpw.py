import os
import tempfile
from os.path import dirname, join

import pytest

from pyunpack import Archive, PatoolError, cli

DIR = dirname(__file__)


def tmpdir():
    d = tempfile.mkdtemp(prefix="pyunpack_test_")
    return d


def test_rarpw_err():
    f = join(DIR, "testpw.rar")

    d = tmpdir()
    with pytest.raises(PatoolError):
        cli.extractall(f, d)


def ok_file(d):
    full = join(d, "rar.txt")
    assert os.path.exists(full)
    assert open(full).read() == "pyunpack rar test with password\n"


def test_rarpw():
    f = join(DIR, "testpw.rar")
    password = "123"

    d = tmpdir()
    Archive(f, backend="patool", password=password).extractall(d)
    ok_file(d)

    d = tmpdir()
    Archive(f, password=password).extractall(d)
    ok_file(d)

    d = tmpdir()
    Archive(f, backend="auto", password=password).extractall(d)
    ok_file(d)

    d = tmpdir()
    cli.extractall(f, d, password=password)
    ok_file(d)
