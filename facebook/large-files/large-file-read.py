import sys

def read_in_chunks(file_desc, chunksize=5000):
    while True:
        data = file_desc.read(chunksize)
        if not data:
            return
        yield data

f, leftover  = open(sys.argv[1]), None
for each_chunk in read_in_chunks(f):
    if leftover:
        each_chunk = leftover + each_chunk
    lines = each_chunk.splitlines()
    if not each_chunk.endswith('\n'):
        leftover = lines.pop()
    else:
        leftover = None
    print(lines)
print(leftover)
