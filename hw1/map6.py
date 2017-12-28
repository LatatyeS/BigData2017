#!/usr/bin/env python
# coding=utf-8
import sys

for line in sys.stdin:
    fields = line.split()
    antiNucleus = int(fields[0])
    Pt = float(fields[3])
    print('%s\t%s' % (antiNucleus, Pt))