import sys

c = 0
output = open(sys.argv[1] + "_id" + sys.argv[2] + ".sam", "w")
f = open(sys.argv[1], "r")
alns = f.readlines()
for aln in alns:
    if aln[0] == "@":
        output.write(aln)
    else:
        tmp = aln.split()
        for i in range(0, len(tmp)):
            if tmp[i].split(":")[0] == "PI" and float(tmp[i].split(":")[2]) >= float(sys.argv[2]):
                output.write(aln)
output.close()
