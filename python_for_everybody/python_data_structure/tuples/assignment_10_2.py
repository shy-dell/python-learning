name = 'mbox-short.txt'

if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

d = dict()

for line in handle: 
    if line.startswith('From '):
        words = line.split()
        tstamp = words[5]

        units = tstamp.split(':')
        hr = units[0]

        d[hr] = d.get(hr,0) + 1

lst = sorted([(h,c) for h,c in d.items()])

for key,val in lst:
    print(key,val)