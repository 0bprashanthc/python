"""
Given an array A of N elements. Find the majority element in the array. A
majority element in an array A of size N is an element that appears more than
N/2 times in the array.
"""
def majority(arr):
    hashmap = dict()
    for i in arr:
        if i in hashmap.keys():
            if hashmap[i] >= n/2:
                return i
            else:
                hashmap[i] += 1
        else:
            hashmap[i] = 1
    return -1
