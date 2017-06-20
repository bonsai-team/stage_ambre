import sys, re

# usage : python parser_last.py new_last_CB.sam

f = open(sys.argv[1], 'r')
sam = f.readlines()
tailles = {}
output = open("new_last_CB2.sam", "w")
final = []
aln = {}
for line in sam:
    if line[0] == "@":
        final.append(line)
        continue
    tmp = line.split()
    if tmp[0] in aln:
        aln[tmp[0]].append(line)
    else:
        aln[tmp[0]] = [line]
    cig = re.split('(\d+)', tmp[5])
    length = 0
    for i in range(0, len(cig)):
        if cig[i] == "S":
            length += int(cig[i - 1])
        elif cig[i] == "H":
            length += int(cig[i - 1])
    if tmp[0] in tailles:
        tailles[tmp[0]].append(len(tmp[9]) - length)
    else:
        tailles[tmp[0]] = [len(tmp[9]) - length]
for read in aln:
    i = tailles[read].index(max(tailles[read]))
    final.append(aln[read][i])
output.writelines(final)
