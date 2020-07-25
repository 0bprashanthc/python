"""
Given an array arr of N integers. Find the contiguous sub-array with maximum
sum.
"""
def kadanes(arr):
    max_sofar,max_tillnow = arr[0],arr[0]
    if max(arr) < 0:
        return min(arr)
    for i in range(0,len(arr)):
        max_tillnow += arr[i]
        max_tillnow = max(max_tillnow,arr[i])
        max_sofar = max(max_sofar,max_tillnow)
    return max_sofar
