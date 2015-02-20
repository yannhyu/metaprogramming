def myfilter(function, sequence):
	result = []
	for item in sequence:
		if function(item):
			result.append(item)
	return result

print myfilter(lambda x: x%2==0, range(10))
print myfilter(lambda x: x%2==1, range(20))

def myfilter(function, *sequences):
	result = []
	for items in zip(*sequences):
		if function(*items):
			result.append(items)
	return result