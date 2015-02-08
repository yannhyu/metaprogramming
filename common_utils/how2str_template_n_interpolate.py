import StringIO

text = '''
The quick elusive silver fox jumped over the lazy dog.
The dog was very tired and the fox was quite quick and elusive.
'''

def isalpha(ch):
	return ch.isalpha()

def get_words_count(fp):
	result = {}
	for line in fp:
		for word in line.split():
			word = filter(isalpha, word.lower())
			if word in result:
				result[word] += 1
			else:
				result[word] = 1
	return result

print get_words_count(StringIO.StringIO(text))

print '*' * 11, ' alternative ', '*' * 11
# alternative
from collections import defaultdict

def get_words_count_2(fp):
	result = defaultdict(int)
	for line in fp:
		for word in line.split():
			word = filter(isalpha, word.lower())
			result[word] += 1
	return result	

print get_words_count_2(StringIO.StringIO(text))