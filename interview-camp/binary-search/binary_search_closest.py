#input: [2,3,5,8,9,11]
#x = 7
#output: 8

def binary_search_closest(a,x):
    start, end, result = 0, len(a)-1, 0
    while start <= end:
        mid = start + (end-start)/2
        if abs(x-a[mid]) < abs(x-a[result]):
            result = mid
        if (a[mid] > x) or (a[mid]==x and a[mid-1]==x and mid>0):
            end = mid - 1
        elif a[mid] < x:
            start = mid + 1
        elif a[mid]==x:
            return mid
    return result

a = [2,3,5,8,9,11]
print a
x = int(input("x: "))
r = binary_search_closest(a,x)
print r, a[r]
