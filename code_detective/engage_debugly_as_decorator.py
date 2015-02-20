# engage_debugly_as_decorator.py

from debugly import debug

class FooMath:
    @debug
    def add(a, b):
	    return a + b

    def sub(a, b):
        return a - b

    @debug
    def mul(a, b):
        return a * b

