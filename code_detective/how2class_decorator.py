def add_myproperty(cls):
    cls.myproperty = 'new property magically added by decorator'
    return cls

@add_myproperty
class MyClass(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return 'MyClass(%r, %r)' % (a.b)

print MyClass
print MyClass.myproperty
