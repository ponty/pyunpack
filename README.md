unpack archive files in Python

Links:
 * home: https://github.com/ponty/pyunpack
 * PYPI: https://pypi.python.org/pypi/pyunpack

[![Build Status](https://travis-ci.org/ponty/pyunpack.svg?branch=master)](https://travis-ci.org/ponty/pyunpack)

Features:
 - unpack archive files without password
 - very simple interface
 - command line interface and library
 - supported python versions: 2.7, 3.6, 3.7, 3.8
 - back-ends: 
    * [zipfile][2]: included in Python
    * [patool][1]: 
      It relies on helper applications to handle those archive formats 
      (for example bzip2 for BZIP2 archives).
      Supported formats:
      7z (.7z), ACE (.ace), ALZIP (.alz), AR (.a), ARC (.arc), ARJ (.arj), 
      BZIP2 (.bz2), CAB (.cab), compress (.Z), CPIO (.cpio), DEB (.deb), 
      DMS (.dms), GZIP (.gz), LRZIP (.lrz), LZH (.lha, .lzh), LZIP (.lz), 
      LZMA (.lzma), LZOP (.lzo), RPM (.rpm), RAR (.rar), RZIP (.rz), 
      TAR (.tar), XZ (.xz), ZIP (.zip, .jar) and ZOO (.zoo)  
 

Functionality
-------------

[patool][1] is called by pyunpack using its command line interface.
If [patool][1] is not installed then only zip format can be unpacked
using the internal python [zipfile][2] library.

 
Usage
=====

    $ echo hello > hello.txt
    $ zip hello.zip hello.txt
    $ rm hello.txt
    $ python3
    >>> from pyunpack import Archive
    >>> Archive('hello.zip').extractall('.')
    >>> open('hello.txt').read()
    'hello\n'

or on console:

    $ echo hello > hello.txt
    $ zip hello.zip hello.txt
    $ rm hello.txt
    $ python3 -m pyunpack.cli hello.zip .
    $ cat hello.txt 
    hello

Installation on Ubuntu
======================

    sudo apt-get install unzip unrar p7zip-full
    pip3 install patool
    pip3 install pyunpack


command line help
==================

    $ python3 -m pyunpack.cli --help
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


[1]: http://pypi.python.org/pypi/patool
[2]: http://docs.python.org/library/zipfile.html
