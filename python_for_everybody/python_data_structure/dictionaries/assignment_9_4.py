name = 'mbox-short.txt'
d = dict()

if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

for line in handle:
    if line.startswith('From '):
        words = line.split()
        target = words[1]

        d[target] = d.get(target,0) + 1

lgst_num = None
lgst_em = None
for email, count in d.items():
    if lgst_num is None or count > lgst_num:
        lgst_num = count
        lgst_em = email

print(lgst_em, lgst_num)