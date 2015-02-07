#!/usr/bin/python -tt

import sys

def Hey(name):
    if name == 'Ian':
        print 'caution: Ian Mode'
        name = name + '???'
    else:
        print 'Else'
    name = name + '!!'
    print 'Hey', name, 'from skeleton..'

def main():
    Hey(sys.argv[1])

# the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()


