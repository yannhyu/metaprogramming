colors = ['red', 'green', 'blue', 'red', 'green', 'red']

d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1

print d

