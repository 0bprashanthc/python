def read(f):
    for line in f.readlines():
        yield line

f = open('test.txt')
r = read(f)
for line in r:
    print(line)
f.close()
