#!/usr/bin/env python

import os
import sys

import pprint

pprint.pprint([os.environ, sys.argv, os.getpid()], stream=sys.stderr)

sys.stdout.write(str(os.getpid()) + os.linesep)

for line in sys.stdin.readlines():
    sys.stdout.write(line)
    sys.stdout.flush()
