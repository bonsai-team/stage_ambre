from Bio import SeqIO
import sys

c = 0
tot = 0
maxi = 0
too_long = 0
for records in SeqIO.parse(sys.argv[1], "fasta"):
    if len(records.seq) < 18:
        c += 1
    if len(records.seq) > 50000:
        too_long += 1
    if len(records.seq) > maxi:
        maxi = len(records.seq)
    tot += 1
print("Nombre de seq < 18 :")
print(c)
print("Nombre total de seq :")
print(tot)
print("Read le plus grand :")
print(maxi)
print("Reads de taille > 50 000:")
print(too_long)
