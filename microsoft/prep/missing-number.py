"""
Given an array C of size N-1 and given that there are numbers from 1 to N with
one element missing, the missing number is to be found.
"""
def missing_number(arr):
    i = 0
    while i < len(arr):
        if i == len(arr)-1:
            return -1
        if arr[i+1]-arr[i] > 1:
            return arr[i]+1
    return -1
