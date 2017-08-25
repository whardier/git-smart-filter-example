#!/usr/bin/env python

import os
import sys

import pprint

for line in sys.stdin.readlines():
    sys.stderr.write(repr([os.getpid(), sys.argv, line.strip()]))
    sys.stdout.write(line)
