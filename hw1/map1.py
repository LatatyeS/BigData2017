#!/usr/bin/env python
# coding=utf-8
import sys

for line in sys.stdin:
    fields = line.split()
    antiNucleus = int(fields[0][:-1])
    eventFile = int(fields[1][:-1])
    prodTime = float(fields[10][:-1])
    Pt = float(fields[11][:-1])
    print('%s\t%s\t%s\t%s' % (antiNucleus, eventFile, prodTime, Pt))