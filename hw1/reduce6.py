#!/usr/bin/env python
# coding=utf-8
import sys

cur_nucl = None
cur_sum = 0.0
cur_count = 0
nucl = None

for line in sys.stdin:
	fields = line.split('\t')
	antiNucleus = int(fields[0])
	Pt = float(fields[1])
	if cur_nucl == None:
		cur_sum = Pt
		cur_count = 1
		cur_nucl = antiNucleus
	elif cur_nucl == antiNucleus:
		cur_sum += Pt
		cur_count += 1
	elif cur_nucl != antiNucleus:
		print('%s\t%s' % (cur_nucl, cur_sum / cur_count))
		cur_sum = Pt
		cur_count = 1
		cur_nucl = antiNucleus

if cur_nucl == nucl:
    print('%s\t%s' % (cur_nucl, cur_sum / cur_count))
