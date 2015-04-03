# only works with python3.4+
from contextlib import redirect_stdout

with open('help.txt', 'w') as f:
    with redirect_stdout(f):
        help(pow)
