import sys

#usage: python correspondance.py aln_megablast.sam

f = open(sys.argv[1], "r")
sam = f.readlines()
f.close()

output = open(sys.argv[1][0:-4] + "_names.sam", "w")
ref = []
for aln in sam:
    if aln[0:3] == "@HD" or aln[0:3] == "@PG":
        output.write(aln)
        continue
    if aln[0:3] == "@SQ":
        output.write(aln)
        ref.append(aln.split()[1][3:])
        continue
    tmp = aln.split()
    tmp[0] = ref[int(tmp[0].split("_")[1]) - 1]
    output.write("\t".join(tmp) + "\n")
output.close()
