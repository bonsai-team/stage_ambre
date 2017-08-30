import sys

# usage : python reads_comparaison.py graphmap.sam bwa.sam

f = open(sys.argv[1], "r")
graphmap = f.readlines()
f.close()
f = open(sys.argv[2], "r")
bwa = f.readlines()
f.close()
g = []
b = []
for aln in graphmap:
    if aln[0] == "@":
        continue
    if aln.split()[0] not in g:
        g.append(aln.split()[0])
for aln in bwa:
    if aln[0] == "@":
        continue
    if aln.split()[0] not in b:
        b.append(aln.split()[0])
commun = 0
for i in g:
    if i in b:
        commun += 1
print("Nombre d'alignements total bwa : {}".format(len(b)))
print("Nombre d'alignements total graphmap : {}".format(len(g)))
print("Nombre d'alignements par les deux : {}".format(commun))
