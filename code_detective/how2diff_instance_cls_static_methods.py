class YourClass():
	def do_this_with_instance(self):
		print 'Instance method called on', self

	@classmethod
	def do_this_with_class(cls):
		print 'Class method called on', cls

	@staticmethod
	def do_this_without_either():
		print 'Static method called'

y = YourClass()
y.do_this_with_instance()
y.do_this_with_class()
y.do_this_without_either()
YourClass.do_this_with_class()

