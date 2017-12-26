#!/usr/bin/env python
# coding=utf-8
import sys

for line in sys.stdin:
    r = line.split()
    antiNucleus = int(r[0])
    prodTime = double(r[2])
    print(‘{}\t{}’.format(antiNucleus, prodTime))