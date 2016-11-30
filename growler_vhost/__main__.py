#!/usr/bin/env python3
#
# growler_vhost/__main__.py
#
"""
Python executable which loads a configuration file and starts a growler server
running a vhost. Forwarding is determined by the configuration file, which has
not been determined yet.
"""

import sys
import logging
from argparse import ArgumentParser


def parser():
    parser = ArgumentParser("growler-vhost")
    parser.add_argument("--daemonize",
                        dest='daemonize',
                        action='store_true',
                        help="Run the processin the background (as a daemon)")
    parser.add_argument("--debug",
                        action='store_true',
                        help="Output debug information")
    return parser


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    args = parser().parse_args(argv)

    logging.basicConfig()
    log = logging.getLogger(__name__)

    if args.debug:
        log.setLevel(logging.DEBUG)

    s = "will" if args.daemonize else "will not"
    log.debug("Process %s daemonize", s)

    return 0


if __name__ == "__main__":
    sys.exit(main())
