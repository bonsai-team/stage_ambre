import sys, re

#usage : python error_rate.py aln.sam

f = open(sys.argv[1], "r")
sam = f.readlines()
f.close()

output = open(sys.argv[1][0:-4] + "_error_rate.txt", "w")
mean = 0
c = 0
for aln in sam:
    if aln[0] == "@":
        continue
    aln = aln.split()
    cig = re.split('(\d+)', aln[5])
    matchs = 0
    clips = 0
    for i in range(0, len(cig)):
        if cig[i] == "S" or cig[i] == "H":
            clips += int(cig[i - 1])
    taille_aln = len(aln[9]) - clips
    for i in range(0, len(aln)):
        if aln[i].split(":")[0] == "NM":
            edit_d = aln[i].split(":")[2]
    error = int(edit_d) / float(taille_aln)
    mean += error
    c += 1
    output.write(str(error) + " " + str(len(aln[9])) + " " + str(taille_aln) + "\n")
output.close()
print("Taux d'erreur moyen : {}%".format(mean / c * 100))
