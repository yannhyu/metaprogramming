class NoInstances(type):
	def __call__(self, *args, **kwargs):
		raise TypeError("Cannot instantiate directly")

# Example usage
class YouCannotInstantiateThis():
	__metaclass__ = NoInstances
	@staticmethod
	def yell(x):
		print 'YouCannotInstantiateThis.yell'


YouCannotInstantiateThis.yell(31)
y = YouCannotInstantiateThis()
