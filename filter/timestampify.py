#!/usr/bin/env python

import os
import sys

import pprint

pprint.pprint(os.environ, sys.stderr, width=1, indent=2)

for line in sys.stdin.readlines():
    sys.stderr.write(repr([os.getpid(), sys.argv, line.strip()]) + os.linesep)
    sys.stdout.write(line + os.linesep)
