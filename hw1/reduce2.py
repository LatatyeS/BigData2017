#!/usr/bin/env python
# coding=utf-8
import sys

current_elem = None
current_sum = 0.0
current_count = 0
elem = None

for line in sys.stdin:
    r = line.split('\t')
    antiNucleus = int(r[0])
    prodTime = double(r[1])
    elem = antiNucleus

    if current_elem is None:
    	current_sum = prodTime
        current_count = 1
        current_elem = elem
    elif current_elem != elem:
    	mean = current_sum / current_count
        print('{}\t{}\t{}'.format(str(current_elem), str(mean), 'mean'))
    elif current_elem == elem:
        current_count += 1
        current_sum += prodTime
            
if current_elem == elem:
    mean = current_sum / current_count
    print('{}\t{}\t{}'.format(str(current_elem), str(mean), 'mean'))