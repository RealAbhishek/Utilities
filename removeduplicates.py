import sys


lineset = set()
filename = sys.argv[1]
filecontent = open(filename, "r")
outfile = open(str(filename)+"-duplicates.csv", "w+")
lines = filecontent.readlines()
for l in lines:
    if l not in lineset:
        lineset.add(l)
    else:
        outfile.write(l)
        outfile.write('\n')

filecontent.close()
outfile.close()
