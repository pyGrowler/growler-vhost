#!/usr/bin/env python
#
# setup.py
#

from setuptools import setup
from importlib.machinery import SourceFileLoader


metadata = SourceFileLoader('metadata', 'growler_vhost/__meta__.py').load_module()

NAME = "growler-vhost"

PACKAGES = [
    'growler_vhost',
    'growler_ext',
]

REQUIRES = [
    'growler'
]

KEYWORDS = [
    'vhost',
    'virtual host',
    'virtual server',
    'reverse proxy',
]

CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "Environment :: Web Environment",
    # "Framework :: Growler",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Topic :: Internet :: WWW/HTTP",
    "Natural Language :: English"
],


setup(
    name=NAME,
    version=metadata.version,
    author=metadata.author,
    license=metadata.license,
    author_email=metadata.author_email,
    description=metadata.description,
    classifiers=CLASSIFIERS,
    install_requires=REQUIRES,
    packages=PACKAGES,
)
