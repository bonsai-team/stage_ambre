import sys
from Bio import SeqIO

#usage : python analyse_mask.py analyse_dustmasker.acclist reads.fa

f = open(sys.argv[1], 'r')
mask = f.readlines()
reads = {}

for r in SeqIO.parse(sys.argv[2], "fasta"):
    reads[r.name] = len(r.seq)

cov = {1:0,2:0,3:0,4:0,5:0}
nb_seq = 0
mean_length = 0
D = []
for m in mask:
    m = m.split()
    mean_length += (int(m[2]) - int(m[1]))
    nb_seq += 1
    if m[0] not in D:
        D.append(m[0])
    pourc = (int(m[2]) - int(m[1])) / float(reads[m[0][1:]])
    if pourc > 0.8:
        cov[5] += 1
    elif pourc > 0.6:
        cov[4] += 1
    elif pourc > 0.4:
        cov[3] += 1
    elif pourc > 0.2:
        cov[2] += 1
    elif pourc > 0:
        cov[1] += 1
print("Nombre de sequences de faible complexite : {}".format(nb_seq))
print("Nombre de reads avec ces sequences : {}".format(len(D)))
print("Taille moyenne de ces sequences : {}".format(mean_length/float(nb_seq)))
print("Classes par rapport au pourcentage des reads : {}".format(cov))
