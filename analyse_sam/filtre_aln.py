#-*- coding: utf-8 -*-
import time, sys, re, os

#usage : python filtre_aln.py aln.sam

pourc = 0.5

f = open(sys.argv[1], "r")
sam = f.readlines()
output = open(os.path.dirname(sys.argv[1]) + "/new_" + os.path.basename(sys.    argv[1]), "w")
start_time = time.time()
compt = 0
nb_aln = 0
sec = 0
unmapped = 0
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
        if (tmp[1] == "4"):
            flag = False
            unmapped += 1
            continue
        if (tmp[13].split(":")[2] != "1"):
            flag = False
            sec += 1
            continue
        cig = re.split('(\d+)', tmp[5])
        taille = 0
        for i in range(0, len(cig)):
            if cig[i] == "S":
                taille += int(cig[i - 1])
        if (len(tmp[9]) * pourc < (len(tmp[9]) - taille) and flag):
            output.write(aln)
        else:
            compt += 1
nb_aln = nb_aln - unmapped
print("Done. Total time in sec : " + str(time.time() - start_time))
print("Il y a " + str(nb_aln) + " alignements au total.")
print("Ce qui représente " + str(nb_aln - sec) + " reads alignés.")
print("On a retiré " + str(compt) + " alignements qui impliquent moins de " + str(pourc * 100) + "% du read")
print("On a retiré " + str(sec) + " alignements secondaires")
print("Il reste maintenant " + str(nb_aln - sec - compt) + " alignements.")
output.close()
f.close()
