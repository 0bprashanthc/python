def getChunk(fileobj):
    chunksize = 1024
    while True:
        data = fileobj.read(1024)
        if not data:
            return
        yield data

def fileRead(filename):
    leftover, fileobj = None, open(filename)
    for chunk in getChunk(fileobj):
        if leftover:
            chunk = leftover+chunk
        lines = chunk.splitlines()
        if not chunk.endswith("\n"):
            leftover = lines.pop()
        else:
            leftover = None
        print(lines)
print(leftover)


