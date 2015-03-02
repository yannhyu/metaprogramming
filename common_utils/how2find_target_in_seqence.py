def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i, value

print find([1,3,5,7,9], 5)
