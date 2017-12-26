#!/usr/bin/env python
# coding=utf-8
import sys

for line in sys.stdin:
    line = line
    fields = line.split('\t')
    if double(fields[2]) > double(fields[4]):
         print(line)