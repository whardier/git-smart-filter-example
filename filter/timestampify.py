#!/usr/bin/env python

import os
import sys

import pprint

buffer = sys.stdin.read()

pprint.pprint([os.getpid(), sys.argv], stream=sys.stderr)

sys.stderr.write(buffer)
sys.stdout.write(buffer)
