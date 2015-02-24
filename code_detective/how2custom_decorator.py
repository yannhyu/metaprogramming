def log_function_call(message):
	def decorator(function):
		def wrapper(*args, **kwargs):
			print '%s: %s(*%r, **%r)' % (message, function, args, kwargs)
			return function(*args, **kwargs)
		print 'returning wrapped %s' % function
		return wrapper
	print 'returning decorator(%r)' % message
	return decorator


@log_function_call('logger1')
def yourfunction(a, b):
	print 'yourfunction(%r, %r)' % (a, b)

yourfunction(10, 23)

