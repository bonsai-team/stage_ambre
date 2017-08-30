import sys

#usage: python parse_sam.py to_parse.sam liste_reads.txt

f = open(sys.argv[1], "r")
sam = f.readlines()
f.close()
f = open(sys.argv[2], "r")
liste = f.readlines()
f.close()
for i in range(0, len(liste)):
    liste[i] = liste[i][:-1]
output = open(sys.argv[1][0:-4] + "_pars.sam", "w")
for aln in sam:
    if aln[0] == "@":
        output.write(aln)
    else:
        tmp = aln.split()
        if tmp[0] in liste:
            output.write(aln)
output.close()
