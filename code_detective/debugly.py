# debugly
# print out info like function name on any function 
# decorated with it

from functools import wraps

def debug(func):
	# func is the function being wrapped
	@wraps(func)
	def wrapper(*args, **kwargs):
		print(func.__qualname__)
		return func(*args, **kwargs)
	return wrapper
