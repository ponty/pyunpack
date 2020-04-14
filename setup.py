from setuptools import setup
import os.path
import sys

NAME = "pyunpack"
URL = "https://github.com/ponty/pyunpack"
DESCRIPTION = "unpack archive files"
PACKAGES = [
    NAME,
    #             NAME + '.examples',
]

# get __version__
__version__ = None
exec(open(os.path.join(NAME, "about.py")).read())
VERSION = __version__


# extra = {}
# if sys.version_info >= (3,):
#     extra['use_2to3'] = True

classifiers = [
    # Get more strings from
    # http://www.python.org/pypi?%3Aaction=list_classifiers
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
]

install_requires = "easyprocess"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    # long_description=open("README.rst", "r").read(),
    classifiers=classifiers,
    keywords="unpack archive",
    author="ponty",
    # author_email='',
    url=URL,
    license="BSD",
    packages=PACKAGES,
    install_requires=install_requires,
    # **extra
)
