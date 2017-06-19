import sys

#usage : python paste_header.py file_with_header.sam file_wo_header.sam

f = open(sys.argv[1], 'r')
header = f.readlines()
H = []
for h in header:
    if h[0] == "@":
        H.append(h)
output = open("output_w_header.sam", "w")
output.writelines(H)
f.close()
f = open(sys.argv[2], 'r')
sam = f.readlines()
output.writelines(sam)
output.close()
f.close()
