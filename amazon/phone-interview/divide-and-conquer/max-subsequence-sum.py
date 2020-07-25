def max_subarray_sum(arr):
    if max(arr) < 0:
        return max(arr)
    max_sofar, max_tillnow = 0,0
    for i in arr:
        max_tillnow += i
        max_tillnow = max(max_tillnow,0)
        max_sofar = max(max_sofar,max_tillnow)
    return max_sofar

if __name__ == "__main__":
    arr = [-2, 3, -4, 5, -7] 
    #arr = [ -8, -3, -6, -2, -5, -4 ]
    print(arr)
    print(max_subarray_sum(arr))

