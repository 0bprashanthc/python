a = [1,2,3,4,5]

start, end = 0, len(a)-1

while start<end:
    a[end],a[start] = a[start],a[end]
    start = start + 1
    end = end - 1
print a
