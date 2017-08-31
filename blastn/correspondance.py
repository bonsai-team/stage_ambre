import sys

#usage: python correspondance.py db.nsd output.sam

f = open(sys.argv[1], "r")
corr = f.readlines()
f.close()
f = open(sys.argv[2], "r")
sam = f.readlines()
f.close()
for i in range(0,len(corr)):
    corr[i] = corr[i].split("\x02")[0]
    corr[i] = corr[i][:-24] + corr[i][-24:].upper()
for i in range(0,len(sam)):
    if sam[i][0] == "@" and sam[i][0:3] != "@SQ":
        continue
    elif sam[i][0:3] == "@SQ":
        try:
            seq = corr[int(sam[i].split()[1].split(":")[1].split("_")[1]) - 1]
        except: continue
        sam[i] = sam[i].split()
        sam[i][1] = sam[i][1][0:3] + seq
        sam[i] = "\t".join(sam[i]) + "\n"
    else:
        sam[i] = sam[i].split()
        if sam[i][0][0:5] == "Query":
            sam[i][0] = corr[int(sam[i][0].split("_")[1]) - 1]
        if sam[i][2][0:5] == "Query":
            print(corr[int(sam[i][2].split("_")[1]) - 1])
            print(sam[i])
            sam[i][2] = corr[int(sam[i][2].split("_")[1]) - 1]
        sam[i] = "\t".join(sam[i]) + "\n"
f = open(sys.argv[2], "w")
f.writelines(sam)
f.close()
