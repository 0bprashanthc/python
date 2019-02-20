a = [-1,-1,2,1,-4,2,3,-1,2]

def find_subarray_with_sum(a,x):
    curr_sum,_map = 0,{}
    for i in range(len(a)):
        curr_sum = curr_sum + a[i]
        if curr_sum == x:
            return (0,i)
        if curr_sum-x in _map:
            return(_map[curr_sum-x]+1, i)
        _map[curr_sum] = i
    return (None, None)
print a
print find_subarray_with_sum(a,0)
