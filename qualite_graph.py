import sys

#usage ; python qualite_graph.py aln.sam liste_reads.txt

f = open(sys.argv[1], "r")
sam = f.readlines()
f.close()

relations = {}
g = open(sys.argv[2], "r")
liste = g.readlines()
g.close()

for r in liste:
    if r.split()[0] in relations:
        relations[r.split()[0]].append([r.split()[1]])
    else:
        relations[r.split()[0]] = r.split()[1]

nb_aln = 0
good = 0
for aln in sam:
    if aln[0] == "@":
        continue
    nb_aln += 1
    if relations[aln.split()[0]] == relations[aln.split()[2]]:
        good += 1
print("sur {} relations : ".format(nb_aln))
print("on a {} relations qui sont bonnes".format(good))
print("donc {} qui sont mauvaises".format(nb_aln - good))
