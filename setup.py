#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2025-2035, Ethan
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from setuptools import setup

desc = "HL7compress: a lightweight Python library to parse, compress and handle HL7 v2.x messages"

long_desc = """
HL7compress: a lightweight Python library to parse, compress and handle HL7 v2.x messages
----------------------------------------------------------------------------------

HL7apy is a lightweight Python package to intuitively handle `HL7 <http://www.hl7.org>`_ v2 messages according to HL7 specifications.

The main features includes:
 * Message parsing
 * Message compression
 * Message decompression
 * Message validation following the HL7 xsd specifications
 * Access to elements by name, long name or position
 * Support to all simple and complex datatypes
 * Encoding chars customization
 * Message encoding in ER7 format and compliant with MLLP protocol
"""


def _get_version():
    with open('VERSION') as f:
        return f.read().strip()


setup(
    name='hl7compress',
    version=_get_version(),
    author='Ethan Wang',
    author_email='ethan.wang2011@gmail.com',
    description=desc,
    long_description=long_desc,
    url='https://github.com/ethan2012/hl7compress',
    license='MIT License',
    python_requires='>=3.6',
    keywords=['HL7', 'Health Level 7', 'healthcare', 'python'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Scientific/Engineering',
    ],
    packages=['hl7compress'],
    test_suite='tests',
)
