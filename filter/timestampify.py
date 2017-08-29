#!/usr/bin/env python

import os
import sys

import pprint

pprint.pprint([os.environ, sys.argv], sys.stderr, width=1, indent=2)

for line in sys.stdin.readlines():
    sys.stdout.write(line)
    sys.stdout.flush()
