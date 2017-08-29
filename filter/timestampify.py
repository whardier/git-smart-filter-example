#!/usr/bin/env python

## For some reason CLEAN is run 3 times during a commit.

import os
import sys

import time

import pprint

#pprint.pprint([os.environ.__dict__, sys.argv, os.getpid()], stream=sys.stderr)

filter = sys.argv[1].upper()
filename = sys.argv[2]

for line in sys.stdin.readlines():

    split_str = line.split('TIMESTAMPIFY:')
    line_str = split_str[0]
    var_str = split_str[-1]

    vars = var_str.strip().split(':')

    cmd = vars[0]

    #Example EPOCH command to replace a variable with an epoch

    if cmd == 'EPOCH':

        clean_var = vars[1]

        if filter == 'CLEAN':

            smudge_var = ('%.3f' % time.time()).replace('.', '')

            line_str = line_str.replace(clean_var, smudge_var)
            var_str = var_str.replace(var_str.strip(), 'TIMESTAMPIFY:EPOCH:' + clean_var + ':' + smudge_var) #Cheap trick to deal with agnostic line endings

            line = line_str + var_str


    sys.stdout.write(line)
    sys.stdout.flush()
