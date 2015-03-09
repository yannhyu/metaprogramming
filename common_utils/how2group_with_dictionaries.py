names = ['alex', 'josh', 'ian', 'dan', 
         'raymond', 'dana', 'evlyn', 'hudson']

d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)

print d

# another idiom
d2 = {}
for name in names:
    key = len(name)
    d2.setdefault(key, []).append(name)

print d2

# another that is more modern
from collections import defaultdict
dd = defaultdict(list)
for name in names:
    key = len(name)
    dd[key].append(name)

print dd
