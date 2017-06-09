#-*- coding: utf-8 -*-
import sys, time
from Bio import SeqIO

#usage : python reads1Donly.fasta

start_time = time.time()
output = open("output1Donly.fasta", "w")
compt = 0
for record in SeqIO.parse(sys.argv[1], "fasta"):
    if len(record.seq) > 18 and len(record.seq) < 50000:
        output.write(record.format("fasta"))
    else:
        compt += 1
print("Done. Total time in sec : " + str(time.time() - start_time))
print("On a retiré " + str(compt) + " séquences qui bloquaient sortme")
output.close()
