# tail a file (works like tail -f)
import time
def tail(f):
    f.seek(0,2)   # move to EOF
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


# look for a specific substring in a sequence of lines
def grep(lines, searchtext):
    for line in lines:
        if searchtext in line:
            yield line

# sample use
serverlog = tail(open("idx.log"))
errlines = grep(serverlog, "MemberExportWorker")
for line in errlines:
    print line,
