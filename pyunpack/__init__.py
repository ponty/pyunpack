from easyprocess import Proc
from path import path
import logging
import os
import sys
import zipfile

__version__ = '0.0.2'

log = logging.getLogger(__name__)
#log=logging

log.debug('version=' + __version__)

class PatoolError(Exception):
    pass

def check_patool():
    try:
        import patoolib
        ok = True
    except ImportError:
        ok = False
        log.debug('patool was not found')
    return ok

class Archive(object):
    '''
    :param backend: ``auto``, ``patool`` or ``zipfile``
    :param filename: path to archive file       
    '''
    def __init__(self, filename, backend='auto'):
        self.filename = path(filename).expand().abspath()
        self.backend = backend
              
    def extractall_patool(self, directory): 
        log.debug("starting backend patool")
        p = Proc([
                         'patool',
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
        
    def extractall(self, directory, auto_create_dir=False): 
        '''
        :param directory: directory to extract to
        :param auto_create_dir: auto create directory
        '''       
        log.debug("extracting %s into %s (backend=%s)" % (self.filename, directory, self.backend))
        is_zipfile = zipfile.is_zipfile(self.filename)
        directory = path(directory).expand().abspath()
        if not self.filename.exists():
            raise ValueError("archive file does not exist:" + str(self.filename))
        if not directory.exists():
            if auto_create_dir:
                directory.makedirs()
            else:
                raise ValueError("directory does not exist:" + str(directory))
            
        if self.backend == 'auto':
            if is_zipfile:
                try:
                    self.extractall_zipfile(directory)
                except AttributeError:
                    # py25
                    self.extractall_patool(directory)                    
            elif check_patool():
                self.extractall_patool(directory)
            else:
                raise ValueError("no backend for archive file:" + str(self.filename))
            
        if self.backend == 'zipfile':
            if not is_zipfile:
                raise ValueError("file is not zip file:" + str(self.filename))
            self.extractall_zipfile(directory)
            
        if self.backend == 'patool':
            if check_patool():
                self.extractall_patool(directory)
            else:
                raise ValueError("patool is not installed")
