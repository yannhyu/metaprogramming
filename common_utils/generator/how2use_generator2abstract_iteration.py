def interesting_lines(f):
	for line in f:
		line = line.strip()
		if line.startswith('#'):
			continue
		if not line:
			continue
		yield line


with open('a_simple_generator.py') as f:
	for line in interesting_lines(f):
		print line