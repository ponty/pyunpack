import glob
import logging
import os

from easyprocess import EasyProcess
from entrypoint2 import entrypoint

commands = """
python3 -m pyunpack.cli --help
"""


commands = commands.strip().splitlines()


def empty_dir(dir):
    files = glob.glob(os.path.join(dir, "*"))
    for f in files:
        os.remove(f)


@entrypoint
def main():
    gendir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gen")
    logging.info("gendir: %s", gendir)
    os.makedirs(gendir, exist_ok=True)
    empty_dir(gendir)
    try:
        os.chdir("gen")
        for cmd in commands:
            logging.info("cmd: %s", cmd)
            fname_base = cmd.replace(" ", "_")
            fname = fname_base + ".txt"
            logging.info("cmd: %s", cmd)
            print("file name: %s" % fname)
            with open(fname, "w") as f:
                f.write("$ " + cmd + "\n")

                p = EasyProcess(cmd).call()
                f.write(p.stdout)
                if p.stderr and p.stdout:
                    f.write("\n")
                f.write(p.stderr)
    finally:
        os.chdir("..")

    embedme = EasyProcess(["npx", "embedme", "../README.md"])
    embedme.call()
    print(embedme.stdout)
    assert embedme.return_code == 0
    assert not "but file does not exist" in embedme.stdout
