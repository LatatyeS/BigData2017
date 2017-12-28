#!/usr/bin/env python
# coding=utf-8
import sys

for line in sys.stdin:
    fields = line.split('\t')
    prodTime = float(fields[2])
    mean_prodTime = float(fields[4])
    if prodTime > mean_prodTime:
         print(line)