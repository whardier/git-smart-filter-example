#!/usr/bin/env python

import os
import sys

import pprint

#pprint.pprint([os.environ, sys.argv], stream=sys.stderr)

for line in sys.stdin.readlines():
    sys.stdout.write(line)
    sys.stdout.flush()
