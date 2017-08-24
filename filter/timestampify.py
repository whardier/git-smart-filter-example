#!/usr/bin/env python

import os
import sys

import json

a = open('/tmp/wut.txt', 'w')
a.write(json.dumps([os.environ], indent=4) + os.linesep)
a.write(json.dumps([sys.argv], indent=4) + os.linesep)
a.write(json.dumps([sys.stdin.read()], indent=4) + os.linesep)
a.close()


