import logging

from entrypoint2 import entrypoint

from pyunpack import Archive

log = logging.getLogger(__name__)
# log=logging


@entrypoint
def extractall(
    filename, directory, backend="auto", password=None, auto_create_dir=False
):
    """
    :param backend: auto, patool or zipfile
    :param filename: path to archive file
    :param directory: directory to extract to
    :param auto_create_dir: auto create directory
    """
    Archive(filename, backend, password=password).extractall(
        directory, auto_create_dir=auto_create_dir
    )
