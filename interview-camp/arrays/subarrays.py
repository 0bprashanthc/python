#find contiguous subarray from an array 
# of positive integers that sums to X. Return indices
a = [2,1,4,5,3,5,1,2,4]
def find_subarray_for_sum(a, x):
    start,end,_sum = -1,-1,0
    while start < len(a):
        if _sum < x:
            end = end + 1
            if end < len(a):
                _sum = _sum + a[end]
        elif _sum > x:
            start = start + 1
            if start < len(a):
                _sum = _sum - a[start]
        else:
            return (start+1, end)
    return (None, None)
print a
x = int(input("x:"))
print find_subarray_for_sum(a,x)
