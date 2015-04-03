# primitive
print '++++++ hey primitive ++++'
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


rev = Reverse("howaboutnow")
for char in rev:
    print char

# generator
print '++++++ hey generator ++++'

def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]

revgen = reverse("howaboutnow")
for char in revgen:
    print char

# generator expression
print '++++++ hey generator expression ++++'
data = "howaboutnow"
for char in list(data[i] for i in range(len(data) - 1, -1, -1)):
    print char





















