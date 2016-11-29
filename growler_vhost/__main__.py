#!/usr/bin/env python3
#
# growler_vhost/__main__.py
#
"""
Python executable which loads a configuration file and starts a growler server
running a vhost. Forwarding is determined by the configuration file, which has
not been determined yet.
"""

from argparse import ArgumentParser

parser = ArgumentParser("growler-vhost")
parser.add_argument("--no-deamon",
                    dest='daemonize',
                    action='store_false',
                    help="Will not deamonize the process")

args = parser.parse_args()

print("Process will%sdeamonize" % (" " if args.daemonize else " not "))
