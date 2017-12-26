#!/usr/bin/env python
# coding=utf-8
import sys

lines = []
for line in sys.stdin:
    lines.append(line.strip())

means = {}
for line in lines:
    fields = line.split('\t')
    if len(fields) == 4 and fields[3] == 'mean':
		means[int(fields[1])] = Decimal(fields[2])


for line in lines:
    fields = line.split('\t')
    if len(fields) == 4 and fields[3] == 'mean':
        continue  
    print('{}\t{}'.format('\t'.join(fields[1:]),means[int(fields[1])]))