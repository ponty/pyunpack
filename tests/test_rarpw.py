import tempfile
from os.path import dirname, join

import pytest

from pyunpack import PatoolError, cli

DIR = dirname(__file__)


def tmpdir():
    d = tempfile.mkdtemp(prefix="pyunpack_test_")
    return d


def test_rarpw():
    f = join(DIR, "testpw.rar")

    d = tmpdir()
    with pytest.raises(PatoolError):
        cli.extractall(f, d)
