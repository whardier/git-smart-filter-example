#!/usr/bin/env python

import os
import sys

import pprint

a = open('/tmp/wut.txt', 'w')
a.write(pprint.pformat([os.environ], width=1) + os.linesep)
a.write(pprint.pformat([sys.argv], width=1) + os.linesep)
a.write(pprint.pformat([sys.stdin.read()], width=1) + os.linesep)
a.close()


