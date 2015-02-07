#!/usr/bin/python -tt

import sys

def Hey(name):
    if name == 'Ian':
        print 'Caution: Ian Mode'
        name = name + '???'
    else:
        print 'Normal Mode:'
    name = name + '!!'
    print 'Hey', name, 'from skeleton..'

def main():
    name = 'World'
    # Get the name from the command line, using 'World' as a fallback.
    if len(sys.argv) >= 2:
        name = sys.argv[1]
    Hey(name)

# the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()


