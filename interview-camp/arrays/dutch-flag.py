#Dutch-National-Flag Problem
#l = [1,2,3,3,4,4,4,5,4,332,124,24,4,4,2134,213,313,2,1]
#n = 9
#   l =[ <n  ,=n,  >n ]

a=[3,5,2,6,8,4,4,6,4,4,3]
a=[1,2,3,3,4,4,4,5,4,332,124,24,4,4,2134,213,313,2,1]
a=[1,4,7,13,54,104,454,5,1,6,4,3,100,20,1]
a=[1,4,7,13,54,104,454,5,1,6,4,3,100,20,1]
a=[1,0,1,2,1,0,1,2]
a= [2,3,0,3,0,1,0]
i = 0

#output: [2,3,3,4,4,4,4,5,6,6,8]
print a
reader, low = 0,0
high = len(a)-1
while reader <= high:
    if a[reader] < i:
        tmp = a[low]
        a[low] = a[reader]
        a[reader] = tmp
        low = low + 1
        reader = reader + 1
    elif a[reader] == i:
        reader = reader + 1
    elif a[reader] > i:
        tmp = a[high]
        a[high] = a[reader]
        a[reader] = tmp
        high = high - 1
print low, reader, high
print a
