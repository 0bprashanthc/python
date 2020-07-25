"""
Given a sorted and rotated array A of N distinct elements which is rotated at
some point, and given an element K. The task is to find the index of the given
element K in the array A.
"""
def searchSortedRotated(arr,x):
    i = 0
    while i < len(arr):
        if i == len(arr)-1:
            if arr[i]==x:
                return i
            return -1
        if arr[i]>arr[i+1]:
            a1,a2 = arr[:i+1],arr[i:]
            index1,index2 = binarySearch(a1,x),binarySearch(a2,x)
            if index1 != -1:
                return len(a2)+index1-1
            if index2 != -1:
                return index2
    return -1

def binarySearch(arr,x):
    low,high = 0,len(arr)-1
    while low <= high:
        mid = low+(high-low)/2
        if arr[mid] > x:
            high = mid-1
        elif arr[mid] > x:
            low = mid+1
        else:
            return mid
    return -1
