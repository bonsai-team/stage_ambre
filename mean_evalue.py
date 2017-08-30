#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

#usage : python mean_evalue.py aln.sam

f = open(sys.argv[1], "r")
sam = f.readlines()
f.close()

evalue = 0
nb_aln = 0
max_evalue = 0.0
min_evalue = 0.0
for aln in sam:
    if aln[0] == "@":
        continue
    nb_aln += 1
    aln = aln.split()
    for i in range(0, len(aln)):
        if aln[i].split(":")[0] == "EV":
            evalue += float(aln[i].split(":")[2])
            if float(aln[i].split(":")[2]) > max_evalue:
                max_evalue = float(aln[i].split(":")[2])
            if float(aln[i].split(":")[2]) < min_evalue:
                min_evalue = float(aln[i].split(":")[2])
print("evalue moyenne : {}".format(evalue/float(nb_aln)))
print("evalue min : {}, evalue max : {}".format(min_evalue, max_evalue))
