#!/usr/bin/env python
# coding=utf-8
import sys

cur_nucl = None
eventFile_set = set()

for line in sys.stdin:
	fields = line.split('\t')
	antiNucleus = int(fields[0])
	eventFile = int(fields[1])

	if cur_nucl == None:
		cur_nucl = antiNucleus
		eventFile_set.add(eventFile)
	elif cur_nucl == antiNucleus:
		eventFile_set.add(eventFile)
	elif cur_nucl != antiNucleus:
		print('%s\t%s' % (cur_nucl, len(eventFile_set)))
		eventFile_set = set([eventFile])
		cur_nucl = antiNucleus

if cur_nucl == nucl:
	print('%s\t%s' % (cur_nucl, len(eventFile_set)))