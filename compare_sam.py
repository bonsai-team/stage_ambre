import sys

print("Lecture du fichier {}".format(sys.argv[1]))
f = open(sys.argv[1], "r")
sam1 = f.readlines()
f.close()

for i in range(0, len(sam1)):
    if sam1[i][0] != "@":
        break
sam1 = sam1[i:]
print("Nombre d'alignements dans ce fichier : {}".format(len(sam1)))
print("Lecture du fichier {}".format(sys.argv[2]))
f = open(sys.argv[2], "r")
sam2 = f.readlines()
f.close()
for i in range(0, len(sam2)):
    if sam2[i][0] != "@":
        break
sam2 = sam2[i:]
print("Nombre d'alignements dans ce fichier : {}".format(len(sam2)))
print("Comparaison des deux SAM")
sam1.sort()
sam2.sort()
meme_chr = 0
exact = 0
aprox = 0
j = 0
i = 0
diff = 0
output = open("liste_reads_diff", "w")
while 1:
    if i >= len(sam1) - 1 or j >= len(sam2) - 1:
        break
    if sam1[i].split()[0] == sam2[j].split()[0]:
        if sam1[i].split()[2] == sam2[j].split()[2]:
            meme_chr += 1
        else:
            diff += 1
            output.write(sam1[i].split()[0] + "\n")
        if sam1[i].split()[3] == sam2[j].split()[3]:
            exact += 1
        elif abs(int(sam1[i].split()[3]) - int(sam2[j].split()[3])) < 5000:
            aprox += 1
        j += 1
        i += 1
    elif sam1[i].split()[0] > sam2[j].split()[0]:
        j += 1
    elif sam1[i].split()[0] < sam2[j].split()[0]:
        i += 1
print("Nombre d'alignements differents : {}".format(diff))
print("Nombre d'alignements sur le meme chr : {}".format(meme_chr))
print("Nombre d'alignements exacts en commun : {}".format(exact))
print("Nombre d'alignements approximativement les memes : {}".format(aprox))
