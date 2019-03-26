#reverse an array without any new list
#Hint: traversal from both ends
#input: [1,2,3,4,5]
#output: [5,4,3,2,1]

a = [1,2,3,4,5]

start, end = 0, len(a)-1

while start<end:
    a[end],a[start] = a[start],a[end]
    start = start + 1
    end = end - 1
print a
