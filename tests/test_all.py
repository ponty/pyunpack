import os
import sys
import tempfile
from shutil import make_archive

import pytest

from pyunpack import Archive, PatoolError, cli

formats = ["zip"]
if sys.platform.startswith("linux"):
    formats += ["tar", "gztar", "bztar", "xztar"]

join = os.path.join


def ok_file(d, f):
    full = join(d, "x.txt")
    assert os.path.exists(full)
    assert open(full).read() == "123"


def tmpdir():
    d = tempfile.mkdtemp(prefix="pyunpack_test_")
    return d


def test():
    with pytest.raises(ValueError):
        Archive("blabla").extractall(tempfile.gettempdir())
    with pytest.raises(PatoolError):
        Archive(__file__).extractall(tempfile.gettempdir())


def create_arc(format):
    d = tmpdir()
    x_txt = join(d, "x.txt")
    open(x_txt, "w").write("123")
    # x_zip = d / "x.zip"

    os.chdir(d)
    x_zip = make_archive(
        "x",
        format,  # the archive format - or tar, bztar, gztar
        root_dir=None,  # root for archive - current working dir if None
        base_dir=None,
    )  # start archiving from here - cwd if None too

    # EasyProcess(["zip", "--no-dir-entries", x_zip, "x.txt"], cwd=d).call()
    return x_zip


def test2():
    for f in formats:
        print(f)
        x_zip = create_arc(f)

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

        if f == "zip":
            d = tmpdir()
            Archive(x_zip, backend="zipfile").extractall(d)
            ok_file(d, "x.txt")

        d = tmpdir()
        cli.extractall(x_zip, d)
        ok_file(d, "x.txt")


def test_subdir():
    for f in formats:
        x_zip = create_arc(f)

        d = join(tmpdir(), "subdir")
        with pytest.raises(ValueError):
            Archive(x_zip).extractall(d, auto_create_dir=False)

        d = join(tmpdir(), "subdir")
        Archive(x_zip, backend="auto").extractall(d, auto_create_dir=True)
        ok_file(d, "x.txt")
