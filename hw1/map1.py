#!/usr/bin/env python
# coding=utf-8
import sys

for line in sys.stdin:
    r = line.split()
    antiNucleus = int(r[0][:-1])
    eventFile = int(r[1][:-1])
    prodTime = double(r[10][:-1])
    Pt = float(r[11][:-1])
    print(‘{}\t{}\t{}\t{}’.format(antiNucleus, eventFile, prodTime, Pt))