import sys

#usage : python verif_composantes.py liste_reads_genes verif_graph.txt

f = open(sys.argv[1], "r")
ref = f.readlines()
f.close()
g = open(sys.argv[2], "r")
graph = g.readlines()
g.close()

D = {} # read : gene,transcrit
for r in ref:
    D[r.split()[0]] = [r.split()[1], r.split()[2]]

res = []
genes = []
transcrits = []
for comp in graph:
    comp = comp.split()
    tmp_g = []
    tmp_t = []
    for read in comp:
        tmp_g.append(D[read][0])
        tmp_t.append(D[read][1])
    res.append(len(set(tmp_g)))
    [genes.append(x) for x in list(set(tmp_g))]
    [transcrits.append(x) for x in list(set(tmp_t))]

print("Nombre de transcrits : {}".format(len(set(transcrits))))
print("Nombre de genes : {}".format(len(set(genes))))
