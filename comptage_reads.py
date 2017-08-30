import sys

f = open(sys.argv[1], "r")
sam = f.readlines()

D = {}
for aln in sam:
    if aln[0] == "@":
        continue
    aln = aln.split()
    D[aln[0]] = 1
print("Nombre de reads alignes : {}".format(len(D.keys())))
