#!/usr/bin/python3 -tt
def coroutine(func):
	def start(*args, **kwargs):
		g = func(*args, **kwargs)
		g.next()
		return g

	return start

# using coroutine decorator
@coroutine
def receiver():
    print('Ready to receive')
    try:
        while True:
            n = (yield)
            print("Got %s" % n)
    except GeneratorExit:
        print('receiver done')


# sample use
r = receiver()
r.send('Hey Ian!')
r.close()
r.send(5)
