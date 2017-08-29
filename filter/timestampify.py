#!/usr/bin/env python

import os
import sys

import pprint
import json

pprint.pprint([os.environ, sys.argv, os.getpid()], stream=sys.stderr)

json.dump(os.environ, open(str(os.getpid()), 'w'), sort_keys=True, indent=2, default=repr)

sys.stdout.write(str(os.getpid()) + os.linesep)

filter = sys.argv[1]
filename = sys.argv[2]

for line in sys.stdin.readlines():
    sys.stdout.write(line)
    sys.stdout.flush()
