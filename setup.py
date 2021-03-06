#!/usr/bin/env python

import ast
from distutils import core


def version():
    """Return version string."""
    with open('libmodernize/__init__.py') as input_file:
        for line in input_file:
            if line.startswith('__version__'):
                return ast.parse(line).body[0].value.s


with open('README.rst') as readme:
    core.setup(
        name='modernize',
        author='Armin Ronacher',
        author_email='armin.ronacher@active-4.com',
        version='0.3',
        url='http://github.com/mitsuhiko/python-modernize',
        packages=['libmodernize', 'libmodernize.fixes'],
        description='A hack on top of 2to3 for modernizing code for '
                    'hybrid codebases.',
        long_description=readme.read(),
        scripts=['python-modernize'],
        classifiers=[
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7'
            'Programming Language :: Python :: 2.6'
            'Programming Language :: Python :: 3.2'
            'Programming Language :: Python :: 3.3'
        ]
    )
