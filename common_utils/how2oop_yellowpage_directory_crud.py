class Directory(object):
    """docstring for Directory"""
    def __init__(self):
        self._directory = {}

    def add_number(self, name, number):
        self._directory[name] = number

    def remove_number(self, name):
        self._directory.pop(name, None)

    def lookup_number(self, name):
        return self._directory.get(name, '<<unknown>>')

    def print_directory(self):
        print 'Start directory'
        print self._directory
        for name, number in self._directory.items():
            print '    %s: %s' % (name, number)
        print 'Finish directory' 

# test code
d = Directory()
d.add_number('Ian', '770-888-9876')
print 'Ian has number', d.lookup_number('Ian')

d.print_directory()
print
d.remove_number('Ian')
d.print_directory()
print
print 'Ian has number', d.lookup_number('Ian')
print
d.remove_number('Ian')

