def log(format, *args, **kwargs):
    if args:
        print format % args
    else:
        print format % kwargs


if __name__ == '__main__':
    log('The pair is (%r, %r)', 1, 2)
    log('The value of a is %(a)r', a='bar')
    log('The value of a is %(a)r', **{'a': 'bar'})
    log('This one does not have any arguments')
