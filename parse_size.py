import sys, re

#python parse_evalue.py aln.sam taille

f = open(sys.argv[1], "r")
alns = f.readlines()
output = open(sys.argv[1][0:-4] + "_size" + sys.argv[2] + ".sam", "w")
for aln in alns:
    if aln[0] == "@":
        output.write(aln)
        continue
    tmp = aln.split()
    if len(tmp[9]) > int(sys.argv[2]):
        output.write(aln)
f.close()
output.close()
