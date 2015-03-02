colors = ['red', 'green', 'blue', 'yellow', 'orange']

print colors
print sorted(colors, key=len)

def getKey(item):
    return item[0]


l = [[2, 3], [6, 7], [3, 34], [24, 64], [1, 43]]
print sorted(l, key=getKey)
