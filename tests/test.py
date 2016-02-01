from easyprocess import EasyProcess
from nose.tools import ok_, eq_, assert_raises
from path import Path
from pyunpack import Archive, PatoolError, cli
import sys
import tempfile


def ok_file(d, f):
    full = d / 'x.txt'
    ok_(full.exists(), full)
    eq_(full.text(), '123')


def tmpdir():
    d = tempfile.mkdtemp(prefix='pyunpack_test_')
    return Path(d)


def test():
    assert_raises(ValueError, lambda: Archive('blabla').extractall('/tmp'))
    assert_raises(PatoolError, lambda: Archive(__file__).extractall('/tmp'))


def create_zip():
    d = tmpdir()
    x_txt = d / 'x.txt'
    x_txt.write_text('123')
    x_zip = d / 'x.zip'
    EasyProcess(['zip', '--no-dir-entries', x_zip, 'x.txt'], cwd=d).call()
    return x_zip


def test2():
    x_zip = create_zip()

    assert_raises(ValueError, lambda: Archive(x_zip).extractall('blabla'))

    d = tmpdir()
    Archive(x_zip, backend='patool').extractall(d)
    ok_file(d, 'x.txt')

    d = tmpdir()
    Archive(x_zip).extractall(d)
    ok_file(d, 'x.txt')

    d = tmpdir()
    Archive(x_zip, backend='auto').extractall(d)
    ok_file(d, 'x.txt')

    if sys.version_info >= (2, 6):
        d = tmpdir()
        Archive(x_zip, backend='zipfile').extractall(d)
        ok_file(d, 'x.txt')

    d = tmpdir()
    cli.extractall(x_zip, d)
    ok_file(d, 'x.txt')


def test_subdir():
    x_zip = create_zip()

    d = tmpdir() / 'subdir'
    assert_raises(ValueError, lambda: Archive(
        x_zip).extractall(d, auto_create_dir=False))

    d = tmpdir() / 'subdir'
    Archive(x_zip, backend='auto').extractall(d, auto_create_dir=True)
    ok_file(d, 'x.txt')
