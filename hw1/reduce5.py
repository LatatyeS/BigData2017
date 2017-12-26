#!/usr/bin/env python
# coding=utf-8
import sys

cur_nucl = None
eventFile_set = None
nucl = None

for line in sys.stdin:
    line = line.strip()
    params = line.split('\t')
    antiNucleus = int(params[0])
    eventFile = int(params[1])
    nucl = antiNucleus
    if cur_nucl == nucl:
	eventFile_set.add(eventFile)
    else:
        if cur_nucl is not None:
            print ('%s\t%s' % (str(cur_nucl), len(eventFile_set)))
        eventFile_set = set()
	eventFile_set.add(eventFile)
        cur_nucl = nucl

if cur_nucl == nucl:
    print ('%s\t%s' % (str(cur_nucl), len(eventFile_set)))