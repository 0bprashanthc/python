"""
Given an array of integers, replace each even number in the array with 2 of same number
input: [2,4,1,0,3]
output: [2,2,4,4,1,0,0,3]
"""
def duplicate_even(a):
    n_even = count_even(a)
    end = len(a)-1
    a.extend([None]*n_even)
    i = len(a)-1
    print a
    while i >= 0:
        if a[end] % 2 == 0:
            a[i] = a[end]
            a[i-1] = a[end]
            i = i - 2
        if a[end] % 2 != 0:
            a[i] = a[end]
            i = i - 1
        end = end - 1
    return a

def count_even(a):
    count = 0
    for i in range(0,len(a)):
        if a[i]%2==0:
            count += 1
    return count

if __name__ == "__main__":
    a = [2,4,1,0,3]
    print duplicate_even(a)
