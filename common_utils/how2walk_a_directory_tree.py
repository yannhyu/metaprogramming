import os

for root, dirs, files in os.walk('/home/ian/Documents/ian_github'):
    print root
    print dirs
    print files