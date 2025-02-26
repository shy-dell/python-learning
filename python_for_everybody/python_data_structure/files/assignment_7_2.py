# Use the file name mbox-short.txt as the file name
count = 0
total = 0

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    num = float(line[-6:])
    total = total + num

avg = float(total / count)

print("Average spam confidence:",avg)