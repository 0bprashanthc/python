#move all ZEROS in the list to the end
#l = [1,2,3,3,4,4,4,5,4,332,124,24,4,4,2134,213,313,2,1]
#n = 9
#   l =[ n,  0 ]

a= [2,3,0,3,0,1,0]
a=[1,0,1,2,1,0,1,2]
i = 0
print a
reader = 0
high = len(a)-1
while reader <= high:
    if a[reader] == i:
        tmp = a[high]
        a[high] = a[reader]
        a[reader] = tmp
        high = high - 1
    else:
        reader = reader + 1
print reader, high
print a
