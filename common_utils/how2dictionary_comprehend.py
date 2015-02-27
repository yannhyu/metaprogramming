import os

print {filename: os.path.getsize(filename) for filename in os.listdir('.')}
