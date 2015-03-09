# The class allows to make a sequence of modifications
# to an existing list; however the modifications only
# take effect if no exceptions occur.  Otherwise the
# original list is returned 

class ListTransaction(object):
    def __init__(self, thelist):
        self.thelist = thelist

    def __enter__(self):
        self.workingcopy = list(self.thelist)
        return self.workingcopy

    def __exit__(self, type, value, traceback):
        if type is None:
            self.thelist[::] = self.workingcopy
        return False

# usage
items = [1, 2, 3]
with ListTransaction(items) as working:
    working.append(4)
    working.append(5)
print items    # should produce [1, 2, 3, 4, 5]

try:
    with ListTransaction(items) as working:
        working.append(9)
        working.append(0)
        raise RuntimeError("we're hosed!!")

except RuntimeError:
    pass

print items    # should produce [1, 2, 3, 4, 5]


