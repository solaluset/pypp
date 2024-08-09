#!/usr/bin/env python

import os
import shutil

from setuptools import setup, find_packages

import pypp

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.rst')) as f:
    long_description = f.read()

shutil.copy2(os.path.join(here, "LICENSE.txt"), os.path.join(here, "pypp"))

setup(
    name="pypp-for-pwcp",
    version=pypp.version,
    description="A C99-like preprocessor for Python",
    long_description=long_description,
    author='Niall Douglas and David Beazley',
    url="https://github.com/solaluset/pypp",
    packages=["pypp", "pypp/ply/src/ply"],
    package_data={"pypp": ["LICENSE.txt", "pickled/*"]},
    test_suite='tests',
    entry_points={
        'console_scripts': [ 'pypp=pypp:main' ]
    },
    options={'bdist_wheel':{'universal':True}},
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
)
