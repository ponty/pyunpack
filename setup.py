import os.path

from setuptools import setup

NAME = "pyunpack"

# get __version__
__version__ = None
exec(open(os.path.join(NAME, "about.py")).read())
VERSION = __version__

URL = "https://github.com/ponty/pyunpack"
DESCRIPTION = "unpack archive files"
LONG_DESCRIPTION = """unpack archive files in Python

home: https://github.com/ponty/pyunpack/tree/"""
LONG_DESCRIPTION += VERSION

PACKAGES = [
    NAME,
    #             NAME + '.examples',
]

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

install_requires = ["easyprocess", "entrypoint2"]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
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
