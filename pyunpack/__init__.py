from easyprocess import EasyProcess
from path import Path
import logging
import os
import sys
import zipfile
from pyunpack.about import __version__


log = logging.getLogger(__name__)
log.debug('version=' + __version__)


class PatoolError(Exception):
    pass

def fullpath(cmd):
    for p in os.environ["PATH"].split(os.pathsep):
        fullp = os.path.join(p, cmd)
        if os.access(fullp, os.X_OK):
            return fullp

class Archive(object):
    '''
    :param backend: ``auto``, ``patool`` or ``zipfile``
    :param filename: path to archive file
    '''
    def __init__(self, filename, backend='auto'):
        self.filename = Path(filename).expand().abspath()
        self.backend = backend

    def extractall_patool(self, directory, patool_path):
        log.debug("starting backend patool")
        if not patool_path:
            patool_path=fullpath('patool')
        p = EasyProcess([
                         sys.executable,
                         patool_path,
                         'extract',
                         self.filename,
                         '--outdir=' + directory,
                 #                     '--verbose',
                         ]).call()
        if p.return_code:
            raise PatoolError("patool can not unpack\n" + str(p.stderr))

    def extractall_zipfile(self, directory):
        log.debug("starting backend zipfile")
        zipfile.ZipFile(self.filename).extractall(directory)

    def extractall(self, directory, auto_create_dir=False, patool_path=None):
        '''
        :param directory: directory to extract to
        :param auto_create_dir: auto create directory
        :param patool_path: the path to the patool backend
        '''
        log.debug("extracting %s into %s (backend=%s)" % (
            self.filename, directory, self.backend))
        is_zipfile = zipfile.is_zipfile(self.filename)
        directory = Path(directory).expand().abspath()
        if not self.filename.exists():
            raise ValueError(
                "archive file does not exist:" + str(self.filename))
        if not directory.exists():
            if auto_create_dir:
                directory.makedirs()
            else:
                raise ValueError("directory does not exist:" + str(directory))

        if self.backend == 'auto':
            if is_zipfile:
                self.extractall_zipfile(directory)
            else:
                self.extractall_patool(directory, patool_path)

        if self.backend == 'zipfile':
            if not is_zipfile:
                raise ValueError("file is not zip file:" + str(self.filename))
            self.extractall_zipfile(directory)

        if self.backend == 'patool':
            self.extractall_patool(directory, patool_path)

