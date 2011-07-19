#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2011 Radim Rehurek <radimrehurek@seznam.cz>

"""
Run with:

sudo python ./setup.py install
"""

import os
import sys

from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = 'sqldict',
    version = '1.0',
    description = 'Persistent dict in Python, backed up by sqlite3 and pickle, multithread-safe.',
    long_description = read('README.txt'),

    py_modules = ['sqldict'],

    # there is a bug in python2.5, preventing distutils from using any non-ascii characters :( http://bugs.python.org/issue2562
    author = 'Radim Rehurek', # u'Radim Řehůřek', # <- should really be this...
    author_email = 'radimrehurek@seznam.cz',

    keywords = 'sqlite, persistent dict, anydbm, multithreaded',

    license = 'public domain',
    platforms = 'any',

    classifiers = [ # from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.5',
        'Topic :: Database :: Front-Ends',
    ],

)