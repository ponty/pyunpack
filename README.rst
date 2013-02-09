unpack archive files

Links:
 * home: https://github.com/ponty/pyunpack
 * documentation: http://ponty.github.com/pyunpack
  
Features:
 - unpack archive files without password
 - very simple interface
 - command line interface and library
 - supported python versions: 2.6, 2.7
 - tested only on linux
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
-----------

patool_ is called by pyunpack using its command line interface.
If Patool_ is not installed then only zip format can be unpacked
using the internal python zipfile_ library.

 
Basic usage
============

    >>> from pyunpack import Archive
    >>> Archive('a.zip').extractall('/path/to')

or on console::

    python -m pyunpack.cli a.zip /path/to


Similar projects
================

 * zipfile_: zip only, included in python
 * patool_: many formats, command line only
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
--------

 * install pip_
 * install unpackers for patool_ (optional)
 * install patool_ (optional)
 * install the program::

    # as root
    pip install pyunpack
    


Ubuntu
----------
::

    sudo apt-get install python-pip
    sudo pip install pyunpack
    #optional
    sudo pip install http://downloads.sourceforge.net/project/patool/0.17/patool-0.17.tar.gz
    sudo pip install entrypoint2 # for cli.py
    sudo apt-get install unzip unrar p7zip-full

Uninstall
----------

::

    # as root
    pip uninstall pyunpack


.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pip.openplans.org/
.. _python: http://www.python.org/
.. _patool: http://pypi.python.org/pypi/patool
.. _zipfile: http://docs.python.org/library/zipfile.html