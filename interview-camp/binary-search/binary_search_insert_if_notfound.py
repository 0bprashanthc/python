#input: [1,2,4,5,6,8]
#x: 3
#output: 2

def binary_search_insert_if_notfound(a,x):
    start,end,result = 0,len(a)-1,-1
    while start <= end:
        mid = start + (end-start)/2
        if abs(a[mid]-x) < abs(a[result]-x):
            result = mid
        if abs(a[mid]-x) == abs(a[result]-x):
            if mid < result:
                result = mid
        if (a[mid] > x) or (a[mid]==x and a[mid-1]==x and mid > 0):
            end = mid - 1
        elif a[mid] < x:
            start = mid + 1
        elif a[mid] == x:
            return mid
    return result+1

a = [1,2,4,5,6,8]
print a
x = int(input("x: "))
print binary_search_insert_if_notfound(a,x)
