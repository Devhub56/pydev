#!/usr/bin/env python

from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Calculator app',
    ext_modules=cythonize("calculator.pyx"),
    zip_safe=False,
)