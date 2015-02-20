class MyClass(object):
	def __init__(self):
		self._value = None

	@property
	def yourproperty(self):
		print 'Getting yourproperty'
		return self._value

	@yourproperty.setter
	def yourproperty(self, value):
		print 'Setting yourproperty'
		self._value = value

y = MyClass()
print y.yourproperty
print
y.yourproperty = 50
print y.yourproperty