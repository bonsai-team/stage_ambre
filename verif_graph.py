import sys
from Bio import SeqIO

#usage : python verif_graph.py verif_graph.txt aln.sam ref.fa chr

composantes = 0
same_gene = 0
diff_gene = 0

D = {}
f = open(sys.argv[2], "r")
sam = f.readlines()
f.close()
for aln in sam:
    if aln[0] == "@":
        continue
    tmp = aln.split()
    D[tmp[0]] = tmp[2]
#D : dictionnaire {read1:transcrit1, read2:transcrit2, ...}

genes = []
nb_transcrits = []

reference = {}
for ref in SeqIO.parse(sys.argv[3], "fasta"):
    tmp = ref.description
    if tmp.split()[2].split(":")[2] != sys.argv[4]:
        continue
    reference[tmp.split()[0]] = tmp.split()[3].split(":")[1]
    if reference[tmp.split()[0]] not in nb_transcrits:
        nb_transcrits.append(reference[tmp.split()[0]])
    if tmp.split()[3].split(":")[1] not in genes:
        genes.append(tmp.split()[3].split(":")[1])
#reference : dictionaire {transcrit1 : gene, transcrit2:gene, ...}

c = 0
transcrits = {}
f = open(sys.argv[1], "r")
graph = f.readlines()
for connexes in graph:
    connexes = connexes.split()
    composantes += 1
    flag = True
    ref = reference[D[connexes[0]]]
    for read in connexes:
        c += 1
        if D[read] in transcrits:
            transcrits[D[read]] += 1
        else:
            transcrits[D[read]] = 1
        if reference[D[read]] != ref:
            print(len(connexes))
            diff_gene += 1
            flag = False
            break
        ref = reference[D[read]]
    if flag:
        same_gene += 1
f.close()
print("Nombre de noeuds : {}".format(c))
print("Nombre de composantes du graphe : {}".format(composantes))
print("Nombre de composantes composees uniquement du meme gene : {}".format(same_gene))
print("Nombre de fausses composantes : {}".format(diff_gene))
print("Nombre de transcrits : {}, {}".format(len(transcrits), len(nb_transcrits)))
print("Nombre de genes dans le graphe : {}".format(len(genes)))
