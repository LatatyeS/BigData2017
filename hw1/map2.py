#!/usr/bin/env python
# coding=utf-8
import sys

for line in sys.stdin:
    fields = line.split()
    antiNucleus = int(fields[0])
    prodTime = float(fields[2])
    print('%s\t%s' % (antiNucleus, prodTime))