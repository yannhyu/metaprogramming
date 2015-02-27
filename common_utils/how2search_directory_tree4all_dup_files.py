# Search directory trees for all duplicate files
import os, md5, pprint, hashlib

hashmap = {}  # content signature --> list of filenames

for path, dirs, files in os.walk('.'):
    for filename in files:
        fullname = os.path.join(path, filename)
        with open(fullname) as f:
            d = f.read()
        h = hashlib.md5(d).hexdigest()
        filelist = hashmap.setdefault(h, [])
        filelist.append(fullname)

pprint.pprint(hashmap)
