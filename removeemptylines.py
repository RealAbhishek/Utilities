import sys

filename = sys.argv[1]

outfile = open(str(filename)+str("NoEmpty.csv"), "w+")
with open(filename,'r') as f:
    for line in f:
        if not line.isspace():
            outfile.write(line)

f.close()
outfile.close()
