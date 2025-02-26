# Use words.txt as the file name
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    "File does not exist"

for line in fh:
    line = line.rstrip()
    print(line)