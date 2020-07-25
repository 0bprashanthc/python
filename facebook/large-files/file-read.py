def chunks(filedesc):
    chunksize = 1024
    while True:
        data = filedesc.read(chunksize)
        if not data:
            return
        yield data

f,leftover = open(filename),None
for chunk in chunks(filename):
    if leftover is not None:
        chunk = leftover+chunk
    lines = chunk.splitlines()
    if not chunk.endswith('\n'):
        leftover = lines.pop()
    else:
        leftover = None
    print(lines)
print(leftover)
