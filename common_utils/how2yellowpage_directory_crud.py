def upsert_number(directory, name, number):
    directory[name] = number

def remove_number(directory, name):
    del directory[name]

def lookup_number(directory, name):
    return directory[name]

directory = {}
upsert_number(directory, 'Ian', '404.567.8901')
print lookup_number(directory, 'Ian')
print directory
upsert_number(directory, 'Ian', '404.987.6543')
print lookup_number(directory, 'Ian')
print directory
remove_number(directory, 'Ian')
print directory
print '-'*33

def remove_number_alt(directory, name):
    try:
        del directory[name]
    except KeyError:
        pass # ignore KeyError

def lookup_number_alt(directory, name):
    try:
        return directory[name]
    except KeyError:
        return 'Undefined number'

print "Nobody's number:", lookup_number_alt(directory, 'Nobody')
remove_number_alt(directory, 'Nobody')
print directory


