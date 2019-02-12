"""
Given an array of integers, replace each even number in the array with 2 of same number
input: [2,4,1,0,3]
output: [2,2,4,4,1,0,0,3]
"""
def n_even(l):
    count = 0
    for i in l:
        if i%2==0:
            count+=1
    return count

if __name__ == "__main__":
    l = [2,4,1,0,3]
    i = len(l)-1
    #count of even numbers in list
    c = n_even(l)
    l.extend([None]*c)
    print l
    end = len(l)-1
    while i >= 0:
        if l[i]%2==0:
            l[end] = l[i]
            l[end-1] = l[i]
            end = end -2
        else:
            l[end] = l[i]
            end = end - 1
        i = i - 1
    print l
