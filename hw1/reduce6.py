#!/usr/bin/env python
# coding=utf-8
import sys

cur_nucl = None
cur_sum = 0.0
cur_count = 0
nucl = None

for line in sys.stdin:
    line = line
    params = line.split('\t')
    antiNucleus = int(params[0])
    Pt = float(params[1])
    nucl = antiNucleus
    if cur_nucl is None:
    	cur_sum = Pt
        cur_count = 1
        cur_nucl = nucl
    elif cur_nucl != nucl:
    	mean = cur_sum / cur_count
        print('{}\t{}\t{}'.format(str(cur_nucl), str(mean), 'mean'))
    elif cur_nucl == nucl:
        cur_count += 1
        cur_sum += Pt

if cur_nucl == nucl:
    mean = cur_sum / cur_count
    print ('%s\t%s\t%s' % (str(cur_nucl), str(mean), 'mean'))
