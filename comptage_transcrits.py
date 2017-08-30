import sys
from Bio import SeqIO

#usage : python comptage_transcrits.py aln.sam ref.fa

f = open(sys.argv[1], "r")
sam = f.readlines()
f.close()

genes = {}
for ref in SeqIO.parse(sys.argv[2], "fasta"):
    genes[ref.description.split()[0]] = ref.description.split()[3].split(":")[1]

output = open("liste_reads_genes_transcrits.txt", "w")
D = {}
G = {}
for aln in sam:
    if aln[0] == "@":
        continue
    aln = aln.split()
    D[aln[2]] = 1
    G[genes[aln[2]]] = 1
    output.write(aln[0] + "\t" + genes[aln[2]] + "\t" + aln[2] + "\n")
print("Nombre de transcrits touches : {}".format(len(D.keys())))
print("Nombre de genes touches : {}".format(len(G.keys())))
