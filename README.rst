unpack archive files

Links:
 * home: https://github.com/ponty/pyunpack
 * documentation: http://ponty.github.com/pyunpack
  
Features:
 - unpack archive files without password
 - very simple interface
 - backends: 
    * patool_: optional, can handle a lot of formats using different programs 
    * zipfile_: included in Python
 - command line interface and library
 
Known problems:
 - Python 3 is not supported
 - tested only on linux

Background
-----------

Patool_ is very good at unpacking a lot of archive formats,
but it can not be used as a python library.
pyunpack is a workaround: patool_ is called using its command line interface.
If Patool_ is not installed then only zip format can be unpacked
using the internal python zipfile_ library.
Patool_ should be converted into a library in the future.
 
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


Installation
============

General
--------

 * install setuptools_
 * install unpackers for patool_ (optional)
 * install patool_ (optional, easy_install does not work)
 * install the program::

    # as root
    easy_install pyunpack
    


Ubuntu
----------
::

    sudo apt-get install python-setuptools
    sudo easy_install pyunpack
    #optional
    sudo easy_install http://sourceforge.net/projects/patool/files/0.13/patool-0.13.tar.gz/download
    sudo apt-get install unzip unrar p7zip-full

Uninstall
----------

first install pip_::

    # as root
    pip uninstall pyunpack


.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pip.openplans.org/
.. _python: http://www.python.org/
.. _patool: http://pypi.python.org/pypi/patool
.. _zipfile: http://docs.python.org/library/zipfile.html