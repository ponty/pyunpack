from nose.tools import eq_
from path import path
from pyunpack import Archive, PatoolError, cli
from unittest import TestCase
import tempfile

root = path(__file__).parent.parent
minilib = root / 'paver-minilib.zip'
class Test(TestCase):
    def test(self):
        self.assertRaises(ValueError, lambda :Archive('blabla').extractall('/tmp'))
        self.assertRaises(PatoolError, lambda :Archive(__file__).extractall('/tmp'))
        
        self.assertRaises(ValueError, lambda :Archive(minilib).extractall('blabla'))
        
        Archive(minilib).extractall(tempfile.mkdtemp())
        Archive(minilib, backend='auto').extractall(tempfile.mkdtemp())
        Archive(minilib, backend='zipfile').extractall(tempfile.mkdtemp())
        Archive(minilib, backend='patool').extractall(tempfile.mkdtemp())
        cli.extractall(minilib,tempfile.mkdtemp())