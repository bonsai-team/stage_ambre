import sys, re

#usage : python error_rate.py aln.sam

f = open(sys.argv[1], "r")
sam = f.readlines()
f.close()

output = open(sys.argv[1] + "error_rate.txt", "w")

for aln in sam:
    if aln[0] == "@":
        continue
    aln = aln.split()
    cig = re.split('(\d+)', aln[5])
    matchs = 0
    clips = 0
    for i in range(0, len(cig)):
        if cig[i] == "M" or cig[i] == "=":
            matchs += int(cig[i - 1])
        if cig[i] == "S" or cig[i] == "H":
            clips += int(cig[i - 1])
    taille_aln = len(aln[9]) - clips
    output.write(str(1 - float(matchs) / taille_aln) + " " + str(len(aln[9])) + " " + str(taille_aln) + "\n")
output.close()
