#
# setup.py
#

from setuptools import setup, find_packages

import growler_vhost

NAME = "growler_vhost"

desc = """The Growler vhost server acts as forwarding agent for HTTP requests to
multiple domains hosted from a single server."""

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
    classifiers=CLASSIFIERS
    install_requires=REQUIRES,
    packages=find_packages(exclude=['tests'])
)
