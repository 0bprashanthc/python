"""
Given an array A of N positive integers and another number X. Determine whether
or not there exist two elements in A whose sum is exactly X.
"""
def keyPair(arr,x):
    hashmap = dict()
    for i in range(0,len(arr)):
        if x-arr[i] in hashmap.keys():
            return True
        else:
            hashmap[arr[i]] = True
    return False

