#!/usr/bin/env python

import os
import sys

import pprint

buffer = sys.stdin.read()

sys.stderr.write(buffer)
sys.stdout.write(buffer)
