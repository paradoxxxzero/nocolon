#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright © 2014 Florian Mounier, Kozea

from setuptools import setup
__version__ = '0.0.2'


setup(
    name="nocolon",
    version=__version__,
    description="nocolon is an utf-8 compatible encoding that removes the "
    "need of colons in python files.",
    author="Florian Mounier",
    author_email="paradoxxx.zero@gmail.com",
    packages=['nocolon'],
    provides=['nocolon'],

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3"
    ])
