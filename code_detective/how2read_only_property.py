class YourClass(object):
	def __init__(self, a):
		self._a = a

	@property
	def a(self):
		return self._a

y = YourClass('yvalue')
print y.a
y.a = 'forcedvalue'
print y.a