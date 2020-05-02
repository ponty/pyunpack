import os
import sys
import tempfile
from shutil import make_archive

import pytest
from path import Path

from pyunpack import Archive, PatoolError, cli


def ok_file(d, f):
    full = d / "x.txt"
    assert full.exists()
    assert full.text() == "123"


def tmpdir():
    d = tempfile.mkdtemp(prefix="pyunpack_test_")
    return Path(d)


def test():
    with pytest.raises(ValueError):
        Archive("blabla").extractall(tempfile.gettempdir())
    with pytest.raises(PatoolError):
        Archive(__file__).extractall(tempfile.gettempdir())


def create_zip():
    d = tmpdir()
    x_txt = d / "x.txt"
    x_txt.write_text("123")
    x_zip = d / "x.zip"

    os.chdir(d)
    make_archive(
        "x",
        "zip",  # the archive format - or tar, bztar, gztar
        root_dir=None,  # root for archive - current working dir if None
        base_dir=None,
    )  # start archiving from here - cwd if None too

    # EasyProcess(["zip", "--no-dir-entries", x_zip, "x.txt"], cwd=d).call()
    return x_zip


def test2():
    x_zip = create_zip()

    with pytest.raises(ValueError):
        Archive(x_zip).extractall("blabla")

    d = tmpdir()
    Archive(x_zip, backend="patool").extractall(d)
    ok_file(d, "x.txt")

    d = tmpdir()
    Archive(x_zip).extractall(d)
    ok_file(d, "x.txt")

    d = tmpdir()
    Archive(x_zip, backend="auto").extractall(d)
    ok_file(d, "x.txt")

    if sys.version_info >= (2, 6):
        d = tmpdir()
        Archive(x_zip, backend="zipfile").extractall(d)
        ok_file(d, "x.txt")

    d = tmpdir()
    cli.extractall(x_zip, d)
    ok_file(d, "x.txt")


def test_subdir():
    x_zip = create_zip()

    d = tmpdir() / "subdir"
    with pytest.raises(ValueError):
        Archive(x_zip).extractall(d, auto_create_dir=False)

    d = tmpdir() / "subdir"
    Archive(x_zip, backend="auto").extractall(d, auto_create_dir=True)
    ok_file(d, "x.txt")
