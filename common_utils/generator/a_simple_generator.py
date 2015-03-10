# using a generator to filter out evens
def evens(stream):
    for n in stream:
    	if n % 2 == 0:
    		yield n

numbers = xrange(20)

for n in evens(numbers):
	print n