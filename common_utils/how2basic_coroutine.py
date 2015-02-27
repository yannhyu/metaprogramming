def print_matches(matchtext):
	print 'Looking for', matchtext
	while True:
		line = (yield)
		if matchtext in line:
			print line

matcher = print_matches('python')
matcher.next()  # advance to the first (yield)

matcher.send('Hey world !')
matcher.send("python is very nice.")
matcher.send('blah')
matcher.close()