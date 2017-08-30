#-*- coding: utf-8 -*-
import sys, time
from Bio import SeqIO

#usage : python filtre_transcript.py ref_transcript.fa

start_time = time.time()
output = open("new_" + sys.argv[1], "w")
compt = 0
for record in SeqIO.parse(sys.argv[1], "fasta"):
    if len(record.seq) > 200:
        output.write(record.format("fasta"))
    else:
        compt += 1
print("Done. Total time in sec : " + str(time.time() - start_time))
print("On a retiré " + str(compt) + " séquences < 200 nucléotides")
output.close()
