from easyprocess import Proc
from nose.tools import ok_, eq_
from pyunpack import Archive, PatoolError, cli
from unittest import TestCase
import os.path
import sys
import tempfile

def ok_file(d, f):
    full = os.path.join(d, 'x.txt')
    ok_(os.path.exists(full), full)
    eq_(open(full).read(), '123')

def tmpdir():
    d = tempfile.mkdtemp(prefix='pyunpack_test_')
    return d

class Test(TestCase):
    def test(self):
        self.assertRaises(ValueError, lambda :Archive('blabla').extractall('/tmp'))
        self.assertRaises(PatoolError, lambda :Archive(__file__).extractall('/tmp'))
        
        
    def test2(self):
        d = tempfile.mkdtemp()
        x_txt = os.path.join(d, 'x.txt')
        open(x_txt, 'w').write('123')
        x_zip = os.path.join(d, 'x.zip')
        Proc(['zip', '--no-dir-entries', x_zip, 'x.txt'], cwd=d).call()

        self.assertRaises(ValueError, lambda :Archive(x_zip).extractall('blabla'))

        d = tempfile.mkdtemp()
        Archive(x_zip, backend='patool').extractall(d)
        ok_file(d, 'x.txt')

        d = tempfile.mkdtemp()
        Archive(x_zip).extractall(d)
        ok_file(d, 'x.txt')
        
        d = tempfile.mkdtemp()
        Archive(x_zip, backend='auto').extractall(d)
        ok_file(d, 'x.txt')
        
        if sys.version_info >= (2,6):
            d = tempfile.mkdtemp()
            Archive(x_zip, backend='zipfile').extractall(d)
            ok_file(d, 'x.txt')
        
        d = tempfile.mkdtemp()
        cli.extractall(x_zip, d)
        ok_file(d, 'x.txt')
        
