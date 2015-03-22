#!/usr/bin/python -tt
import weakref

class Cached(type):
	def __init__(self, *args, **kwargs):
		super(Cached, self).__init__(*args, **kwargs)
		self.__cache = weakref.WeakValueDictionary()

	def __call__(self, *args):
		if args in self.__cache:
			return self.__cache[args]
		else:
			obj = super(Cached, self).__call__(*args)
			self.__cache[args] = obj
			return obj



# example usage
class WeGotCache():
	__metaclass__ = Cached

	def __init__(self, name):
		print 'creating WeGotCache({!r})'.format(name)
		self.name = name


a = WeGotCache('Ian')
b = WeGotCache('SomeoneElse')
c = WeGotCache('Ian')

print a is b
print a is c


