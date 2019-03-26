#Given a sorted array A that has been rotated in a cycle, find the smallest element of the array in O(log(n)) time.
#[1,2,4,5,7,8] rotated by 3 gives us A = [5,7,8,1,2,4] and the smallest number is 1

def binary_search_cyclic_list(a,x):
    start,end,right = 0,len(a)-1,a[len(a)-1]
    while start <= end:
        mid = start + (end-start)/2
        if (a[mid]<=right)and(a[mid-1]>a[mid] or mid==0):
            return mid
        if (a[mid]>right):
            start = mid + 1
        else:
            end = mid - 1
    return -1

a = [5,7,8,1,2,4]
print a
x = int(input("x: "))
print binary_search_cyclic_list(a,x)
