import sys

from easyprocess import EasyProcess

help_txt = """
usage: cli.py [-h] [-b BACKEND] [-p PASSWORD] [-a] [--debug]
              filename directory

positional arguments:
  filename              path to archive file
  directory             directory to extract to

optional arguments:
  -h, --help            show this help message and exit
  -b BACKEND, --backend BACKEND
                        auto, patool or zipfile
  -p PASSWORD, --password PASSWORD
  -a, --auto-create-dir
                        auto create directory
  --debug               set logging level to DEBUG
""".strip()
# text changed in py3.10
if sys.version_info[0] > 3 or sys.version_info[1] >= 10:
    help_txt = help_txt.replace("optional arguments", "options")

python = sys.executable


def test_help():
    cmd = [python, "-m", "pyunpack.cli", "--help"]
    h = EasyProcess(cmd).call().stdout.strip()
    h = h.replace("\r", "")  # for win
    print(help_txt)
    print(h)
    assert h == help_txt
