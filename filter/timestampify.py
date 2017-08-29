#!/usr/bin/env python

## For some reason CLEAN is run 3 times during a commit.

import os
import sys

import pprint
import json

pprint.pprint([os.environ.__dict__, sys.argv, os.getpid()], stream=sys.stderr)

json.dump(os.environ.__dict__, open(str(os.getpid()), 'w'), sort_keys=True, indent=2, default=repr)

sys.stdout.write(str(os.getpid()) + os.linesep)

filter = sys.argv[1]
filename = sys.argv[2]

for line in sys.stdin.readlines():
    sys.stdout.write(line)
    sys.stdout.flush()
