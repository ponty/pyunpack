unpack archive files

Links:
 * home: https://github.com/ponty/pyunpack
 * documentation: http://pyunpack.readthedocs.org
 * PYPI: https://pypi.python.org/pypi/pyunpack

|Travis| |Coveralls| |Latest Version| |Supported Python versions| |License| |Downloads| |Code Health| |Documentation|
  
Features:
 - unpack archive files without password
 - very simple interface
 - command line interface and library
 - supported python versions: 2.7, 3.3, 3.4, 3.5
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
 

Background
----------

patool_ is called by pyunpack using its command line interface.
If Patool_ is not installed then only zip format can be unpacked
using the internal python zipfile_ library.

 
Usage
=====

    >>> from pyunpack import Archive
    >>> Archive('a.zip').extractall('/path/to')

or on console::

    python -m pyunpack.cli a.zip /path/to


Similar projects
================

 * zipfile_: zip only, included in python
 * patool_: many formats, command line and library, GPL
 * `python-archive <http://pypi.python.org/pypi/python-archive>`_: zip and tar only
 * `rarfile <http://pypi.python.org/pypi/rarfile/>`_: rar only
 * `pyUnRAR2 <http://pypi.python.org/pypi/pyUnRAR2>`_: rar only
 * `pylzma <http://pypi.python.org/pypi/pylzma>`_: LZMA only
 * `easy-extract <http://pypi.python.org/pypi/easy-extract>`_: many formats, no simple interface for unpacking
 * `python-archive <http://pypi.python.org/pypi/python-archive>`_: zip and tar only
 * `pyarchive <http://pypi.python.org/pypi/pyarchive>`_
 * `nested.tar.archives.extractor <http://pypi.python.org/pypi/nested.tar.archives.extractor>`_: tar only

Installation
============

General
-------

 * install pip_
 * install unpackers for patool_ (optional)
 * install patool_ (optional)
 * install the program::

    # as root
    pip install pyunpack
    


Ubuntu
------
::

    sudo apt-get install python-pip
    sudo pip install pyunpack
    #optional
    sudo pip install patool
    sudo pip install entrypoint2
    sudo apt-get install unzip unrar p7zip-full

Uninstall
---------

::

    # as root
    pip uninstall pyunpack


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


.. _pip: http://pip.openplans.org/
.. _python: http://www.python.org/
.. _patool: http://pypi.python.org/pypi/patool
.. _zipfile: http://docs.python.org/library/zipfile.html

.. |Travis| image:: http://img.shields.io/travis/ponty/pyunpack.svg
   :target: https://travis-ci.org/ponty/pyunpack/
.. |Coveralls| image:: http://img.shields.io/coveralls/ponty/pyunpack/master.svg
   :target: https://coveralls.io/r/ponty/pyunpack/
.. |Latest Version| image:: https://img.shields.io/pypi/v/pyunpack.svg
   :target: https://pypi.python.org/pypi/pyunpack/
.. |Supported Python versions| image:: https://img.shields.io/pypi/pyversions/pyunpack.svg
   :target: https://pypi.python.org/pypi/pyunpack/
.. |License| image:: https://img.shields.io/pypi/l/pyunpack.svg
   :target: https://pypi.python.org/pypi/pyunpack/
.. |Downloads| image:: https://img.shields.io/pypi/dm/pyunpack.svg
   :target: https://pypi.python.org/pypi/pyunpack/
.. |Code Health| image:: https://landscape.io/github/ponty/pyunpack/master/landscape.svg?style=flat
   :target: https://landscape.io/github/ponty/pyunpack/master
.. |Documentation| image:: https://readthedocs.org/projects/pyscreenshot/badge/?version=latest
   :target: http://pyunpack.readthedocs.org

