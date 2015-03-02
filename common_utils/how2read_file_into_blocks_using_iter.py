from functools import partial
with open('hey_skeleton.py') as f:
    blocks = []
    for block in iter(partial(f.read, 32), ''):
        blocks.append(block)

    print blocks
