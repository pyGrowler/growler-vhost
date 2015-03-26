#
# setup.py
#

from setuptools import setup

import growler_vhost

NAME = "growler_vhost"

desc = """The Growler vhost server acts as forwarding agent for HTTP requests to
multiple domains hosted from a single server."""

description = """The Growler vhost server acts as forwarding agent for HTTP
requests to multiple domains hosted from a single server. This is an
implementation of the service using the _Growler_ microframework to handle the
incoming request. As with everything Growler, all events are asynchronous, and
handled when-needed.

This package comes as a binary, which can be run in the form of
`growler-vhost -c <config_file>`, specifying the path to the config file to use
as parameters.

I have a hope that optimizations can be made such that forwarding the request to
another growler server takes (almost) no extra resources. As the request can
easily be parsed once into the format that the growler application already uses.
We are a long way from that, though.
"""

REQUIRES = [
    'growler'
]

KEYWORDS = [
    'vhost',
    'virtual server'
]

CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    # "Framework :: Growler",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Topic :: Internet :: WWW/HTTP",
    "Natural Language :: English"
],


setup(
    name=NAME,
    version=growler_vhost.__version__,
    author=growler_vhost.__author__,
    license=growler_vhost.__license__,
    url=growler_vhost.__version__,
    author_email=growler_vhost.__contact__,
    description=desc,
    long_description=description,
    classifiers=CLASSIFIERS
    install_requires = ['growler'],
    packages = ['growler_vhost']
)
