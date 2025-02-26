fname = 'romeo.txt'
try:
    fh = open(fname)
except:
    print("wrong file name")

lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)

lst.sort()
print(lst)