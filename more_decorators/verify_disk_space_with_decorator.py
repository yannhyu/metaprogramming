# verify_disk_space.py
import os
from functools import wraps

def verify_disk_space(func):
    # func is function to be wrapped
    MINIMUM = 2423009L
    @wraps(func)
    def wrapper(*args, **kwargs):
        #print func.__name__
        # check disk space here
        s = os.statvfs('/home/ian/Documents/GitRepos/IDX/exports')
        available = (s.f_bavail * s.f_frsize) / 1024
        print available
        if available > MINIMUM:
            print "there is enough space..."
            return func(*args, **kwargs)
        else:
            print "there is NOT enough space, abort..."
            pass
    return wrapper


# usage
@verify_disk_space
def add(a, b):
    return a + b


print add(3, 7)
