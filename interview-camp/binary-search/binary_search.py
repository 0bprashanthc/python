#input: [1,2,4,7,8,9]
#x = 2
def binary_search(l,x):
    start,end = 0,len(l)-1
    while ( start <= end ):
        mid = start + (end-start)/2
        if (a[mid] > x) or (a[mid]==x and a[mid-1]==x and mid>0):
            end = mid - 1
        elif a[mid] < x:
            start = mid + 1
        elif a[mid] == x:
            return mid
    return -1
a = [1,2,4,7,8,9]
a = [2,3,4,4,4,4,4,4,4,5,6]
print a
x = int(input("x: "))
print binary_search(a,x)
