#!/usr/bin/env python
# coding=utf-8
"""Setup file for the `gymnasiums` Django project."""

import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    """Retrieves the version from gymnasiums/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


VERSION = get_version("gymnasiums", "__init__.py")
README = open('README.rst').read()

setup(
    name='dj-gymnasiums',
    version=VERSION,
    description="""Django Newsletter for vcn""",
    long_description=README,
    author='Henri Buyse',
    author_email='henri.buyse@gmail.com',
    url='https://github.com/hbuyse/dj-gymnasiums',
    packages=[
        'gymnasiums',
    ],
    include_package_data=True,
    install_requires=[],
    license="MIT",
    zip_safe=False,
    keywords='dj-gymnasiums',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
