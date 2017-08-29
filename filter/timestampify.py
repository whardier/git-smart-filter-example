#!/usr/bin/env python

import os
import sys

import pprint

pprint.pprint(os.environ, sys.stderr, width=1, indent=2)

sys.stdout.write('thisn:' + repr(os.getpid()) + os.linesep)

for line in sys.stdin.readlines():
    sys.stderr.write(repr([os.getpid(), sys.argv, line.strip()]) + os.linesep)
    sys.stdout.write(line + os.linesep)
