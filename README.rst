unpack archive files

Links:
 * home: https://github.com/ponty/pyunpack
 * PYPI: https://pypi.python.org/pypi/pyunpack

|Travis| |License|
  
Features:
 - unpack archive files without password
 - very simple interface
 - command line interface and library
 - supported python versions: 2.7, 3.6, 3.7, 3.8
 - back-ends: 
    * zipfile_: included in Python
    * patool_: 
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

patool_ is called by pyunpack using its command line interface.
If Patool_ is not installed then only zip format can be unpacked
using the internal python zipfile_ library.

 
Usage
=====

    >>> from pyunpack import Archive
    >>> Archive('a.zip').extractall('/path/to')

or on console::

    python -m pyunpack.cli a.zip /path/to

Installation on Ubuntu
======================
::

    sudo apt-get install unzip unrar p7zip-full
    pip3 install patool
    pip3 install pyunpack


command line help
=================

::

  #-- sh('python -m pyunpack.cli --help')--#
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
  #-#


.. _patool: http://pypi.python.org/pypi/patool
.. _zipfile: http://docs.python.org/library/zipfile.html

.. |Travis| image:: https://travis-ci.org/ponty/pyunpack.svg?branch=master
   :target: https://travis-ci.org/ponty/pyunpack/
.. |License| image:: https://img.shields.io/pypi/l/pyunpack.svg
   :target: https://pypi.python.org/pypi/pyunpack/

