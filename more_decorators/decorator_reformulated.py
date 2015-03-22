# only works with python3.3+
from functools import wraps, partial

def debug(func=None, *, prefix=''):
    if func is None:
        return partial(debug, prefix=prefix)

    msg = prefix + func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        print (msg)
        return func(*args, **kwargs)
    return wrapper

# usage as a simple decorator
@debug
def add(a, b):
    return a + b

# usage as a decorator with optional configuration
@debug(prefix='*** ')
def subtract(a, b):
    return a - b

add(3, 5)
subtract(4, 9)


