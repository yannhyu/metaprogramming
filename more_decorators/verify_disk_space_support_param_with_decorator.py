# verify_disk_space.py
import os
from functools import wraps

def verify_disk_space(minimum=10000L):
    '''check disk space before writing big file to it '''
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            #print func.__name__
            # check disk space here
            s = os.statvfs('/home/ian/Documents/GitRepos/IDX/exports')
            available = (s.f_bavail * s.f_frsize) / 1024
            print available
            if available > minimum:
                print "there is enough space..."
                return func(*args, **kwargs)
            else:
                print "there is NOT enough space, abort..."
                pass
        return wrapper
    return decorate


# usage
@verify_disk_space(minimum=442394569L)
def add(a, b):
    return a + b


print add(3, 7)
