#!/usr/bin/env python
# coding=utf-8
import sys

for line in sys.stdin:
    row = line.split()
    antiNucleus = int(row[0])
    Pt = float(row[3])
    print('%s\t%s' % (antiNucleus, Pt))