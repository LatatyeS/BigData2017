#!/usr/bin/env python
# coding=utf-8
import sys

cur_nucl = None
cur_sum = 0.0
cur_count = 0
elem = None

for line in sys.stdin:
    r = line.split('\t')
    antiNucleus = int(r[0])
    prodTime = double(r[1])
    elem = antiNucleus

    if cur_nucl is None:
    	cur_sum = prodTime
        cur_count = 1
        cur_nucl = elem
    elif cur_nucl != elem:
    	mean = cur_sum / cur_count
        print('{}\t{}\t{}'.format(str(cur_nucl), str(mean), 'mean'))
    elif cur_nucl == elem:
        cur_count += 1
        cur_sum += prodTime
            
if cur_nucl == elem:
    mean = cur_sum / cur_count
    print('{}\t{}\t{}'.format(str(cur_nucl), str(mean), 'mean'))