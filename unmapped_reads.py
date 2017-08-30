from Bio import SeqIO
import sys

#usage : python unmapped_reads.py aln.sam reads.fa

f = open(sys.argv[1], "r")
sam = f.readlines()
output = open("unmapped_reads" + sys.argv[1][0:-4] + ".fa", "w")
D = []
for aln in sam:
    if aln.split()[0][0] == "@":
        continue
    if aln.split()[0] not in D:
        D.append(aln.split()[0])
for rec in SeqIO.parse(sys.argv[2], "fasta"):
    if rec.name not in D:
        output.write(rec.format('fasta'))
output.close()
f.close()
