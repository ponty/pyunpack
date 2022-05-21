import os
import tempfile
from os.path import dirname, join

import pytest

from pyunpack import Archive, cli

DIR = dirname(__file__)


def tmpdir():
    d = tempfile.mkdtemp(prefix="pyunpack_test_")
    return d


def test_zippw_err():
    f = join(DIR, "testpw.zip")

    d = tmpdir()
    with pytest.raises(RuntimeError):
        Archive(f).extractall(d)

    d = tmpdir()
    with pytest.raises(RuntimeError):
        Archive(f, password="bad").extractall(d)

    d = tmpdir()
    with pytest.raises(RuntimeError):
        cli.extractall(f, d)


def ok_file(d):
    full = join(d, "zip.txt")
    assert os.path.exists(full)
    assert open(full).read() == "pyunpack zip test with password\n"


def test_zippw():
    f = join(DIR, "testpw.zip")
    password = "123"

    d = tmpdir()
    Archive(f, backend="patool", password=password).extractall(d)
    ok_file(d)

    d = tmpdir()
    Archive(f, backend="zipfile", password=password).extractall(d)
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
