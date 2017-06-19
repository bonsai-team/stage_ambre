import sys

# Compte le nombre de transcrits touches par un aln

f = open(sys.argv[1], 'r')
sam = f.readlines()
transcrits = {}
for aln in sam:
    if aln[0] == "@":
        continue
    aln = aln.split()
    if aln[2] == "*":
        continue
    if aln[2] in transcrits.keys():
        transcrits[aln[2]] += 1
    else:
        transcrits[aln[2]] = 1
print("La couverture verticale est : {}".format(len(transcrits.keys())))
