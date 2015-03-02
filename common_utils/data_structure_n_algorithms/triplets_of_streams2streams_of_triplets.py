names = ['name_1', 'name_2', 'name_3']
colors = ['color_a', 'color_b', 'color_c', 'color_d']
phones = ['123-456-7890', '234-567-8901', '345-678-9012']

for name, color, phone in zip(names, colors, phones):
    print name, '--->', color, '+++>', phone 

# faster
from itertools import izip
for name, color, phone in izip(names, colors, phones):
    print name, '--->', color, '+++>', phone 


# make a new dictionary out of two lists
d = dict(izip(names, phones))
print d

