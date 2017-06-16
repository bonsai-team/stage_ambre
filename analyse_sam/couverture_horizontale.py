import sys, re

# Calcule le nombre de transcrits couverts a (classes) :
# 100% : classe 5
# 80-100% : classe 4
# 60-80% : classe 3
# 40-60% : classe 2
# 20-40% : classe 1
# 0-20% : classe 0

f = open(sys.argv[1], 'r')
sam = f.readlines()

ref_t = {}
tmp = {}
cov = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0}
for aln in sam:
    if aln[0:3] == "@SQ":
        aln = aln.split()
        ref_t[aln[1].split(":")[1]] = int(aln[2].split(":")[1])
        tmp[aln[1].split(":")[1]] = []
    else:
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
        tmp[aln[2]].append(taille)
for ref in ref_t.keys():
    pourc = max(tmp[ref]) / float(ref_t[ref])
    if pourc == 1:
        cov[5] += 1
    elif pourc > 0.8:
        cov[4] += 1
    elif pourc > 0.6:
        cov[3] += 1
    elif pourc > 0.4:
        cov[2] += 1
    elif pourc > 0.2:
        cov[1] += 1
    else:
        cov[0] += 1
print("La couverture horizontale est : {}".format(cov))
