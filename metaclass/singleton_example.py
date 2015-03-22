class Singleton(type):
	def __init__(self, *args, **kwargs):
		self.__instance = None
		super(Singleton, self).__init__(*args, **kwargs)

	def __call__(self, *args, **kwargs):
		if self.__instance is None:
			self.__instance = super(Singleton, self).__call__(*args, **kwargs)
			return self.__instance
		else:
			return self.__instance


# example usage
class YouCanOnlyMakeOne():
	__metaclass__ = Singleton

	def __init__(self):
		print 'Creating the one and only'


a = YouCanOnlyMakeOne()
b = YouCanOnlyMakeOne()
print a is b

