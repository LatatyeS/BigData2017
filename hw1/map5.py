#!/usr/bin/env python
# coding=utf-8
import sys

for line in sys.stdin:
    fields = line.split()
    antiNucleus = int(fields[0])
    eventFile = int(fields[1])
    print('%s\t%s' % (antiNucleus, eventFile))