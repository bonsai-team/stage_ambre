#-*- coding: utf-8 -*-
import time, sys, re

#usage : python filtre_aln.py aln.sam reads.fa

f = open(sys.argv[1], "r")
sam = f.readlines()
output = open("new_" + sys.argv[1], "w")
start_time = time.time()
compt = 0
nb_aln = 0
sec = 0
for aln in sam:
    if aln[0] == "@":
        output.write(aln)
    else:
        nb_aln += 1
        flag = True
        tmp = aln.split()
        if (tmp[1] == "256" or tmp[1] == "2048"):
            flag = False
            sec += 1
            continue
        cig = re.split('(\d+)', tmp[5])
        taille = 0
        for i in range(0, len(cig)):
            if cig[i] == "S":
                taille += int(cig[i - 1])
            elif cig[i] == "H":
                taille += int(cig[i - 1])
        if (len(tmp[9])/2.0 < (len(tmp[9]) - taille) and flag):
            output.write(aln)
        else:
            compt += 1
print("Done. Total time in sec : " + str(time.time() - start_time))
print("Il y a " + str(nb_aln) + " alignements au total.")
print("On a retiré " + str(compt) + " alignements qui impliquent moins de 50% du read")
print("On a retiré " + str(sec) + " alignements secondaires")
print("Il reste maintenant " + str(nb_aln - sec - compt) + " alignements.")
output.close()
f.close()
