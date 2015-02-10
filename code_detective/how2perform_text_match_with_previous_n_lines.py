#!/usr/bin/python3 -tt

# python3.3+ only
# performs a text match on a sequence of lines and
# yield the matching line along with the previous
# N lines of context when found

from collections import deque
def search(lines, pattern, history=6):
    previous_lines = deque(maxlen=history) 
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# for example
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, previous_lines in search(f, 'Fortunately', 3):
            for prevline in previous_lines:
                print(prevline, end='')

            print(line, end='')
            print('+' * 10)

    

