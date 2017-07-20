import sys, re

f = open(sys.argv[1], 'r')
sam = f.readlines()

ref_t = {}
tmp = {}
for aln in sam:
    if aln[0:3] == "@SQ":
        aln = aln.split()
        ref_t[aln[1].split(":")[1]] = int(aln[2].split(":")[1])
        tmp[aln[1].split(":")[1]] = [0]
    else:
        if aln[0] == "@":
            continue
        aln = aln.split()
        if aln[2] == "*":
            continue
        cig = re.split('(\d+)', aln[5])
        taille = 0
        for i in range(0, len(cig)):
            if cig[i] == "S":
                taille += int(cig[i - 1])
            elif cig[i] == "H":
                taille += int(cig[i - 1])
        taille = len(aln[9]) - taille #taille de l'aln
        tmp[aln[2]].append(taille)
output_tot = open(sys.argv[1][0:-4] + "_tot.txt", "w")
output_read = open(sys.argv[1][0:-4] + "_read.txt", "w")
for ref in ref_t.keys():
    for L in tmp[ref]:
        pourc = L / float(ref_t[ref])
        if pourc != 0 and pourc <= 1:
            output_tot.write(str(pourc) + "\n")

for ref in ref_t.keys():
    pourc = max(tmp[ref]) / float(ref_t[ref])
    if pourc != 0 and pourc <= 1:
        output_read.write(str(pourc) + "\n")

cov_vertical = 0
for transcrit in ref_t.keys():
    if not max(tmp[transcrit]) == 0:
        cov_vertical += 1
print("La couverture verticale est de : {}".format(cov_vertical))
