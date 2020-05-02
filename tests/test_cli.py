import sys

from easyprocess import EasyProcess

help = """
usage: cli.py [-h] [-b BACKEND] [-a] [--debug] filename directory

positional arguments:
  filename              path to archive file
  directory             directory to extract to

optional arguments:
  -h, --help            show this help message and exit
  -b BACKEND, --backend BACKEND
                        auto, patool or zipfile
  -a, --auto-create-dir
                        auto create directory
  --debug               set logging level to DEBUG
""".strip()
python = sys.executable


def test_help():
    cmd = [python, "-m", "pyunpack.cli", "--help"]
    h = EasyProcess(cmd).call().stdout.strip()
    h = h.replace("\r", "")  # for win
    print(help)
    print(h)
    assert h == help
