#!/usr/bin/env python
# coding=utf-8
import sys

lines = []
means = {}
for line in sys.stdin:
	fields = line.split('\t')
	if len(fields) == 2:
		key = int(fields[0])
		mean = float(fields[1])
		means[key] = mean
	else:
		lines.append(line)

for line in lines:
    fields = line.split('\t') 
    print('%s\t%s' % (line, means[int(fields[0])]))