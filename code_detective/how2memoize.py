# use decorator to build a useful tool 
# that memoize function results
def memoize(function):
	cache = {}
	def wrapper(*args, **kwargs):
		cache_key = (args, tuple(sorted(kwargs.items())))
		if cache_key in cache:
			print '--- return cached value for', cache_key
			return cache[cache_key]
		result = function(*args, **kwargs)
		cache[cache_key] = result
		return result
	return wrapper

@memoize
def optimized_function(a, b):
	print 'Calling optimized_function(%r, %r)' % (a, b)
	return a + b


print optimized_function(8, 9)
print optimized_function(8, 9)
print optimized_function(8, 9)

print optimized_function(2, 1)
print optimized_function(4, 3)
print optimized_function(6, 5)