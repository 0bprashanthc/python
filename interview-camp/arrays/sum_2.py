#find two elements in the list which when added returns X
#return the indices of the elements in the list
#input: [1,2,3,4,5,6,7], X = 8
#output: (1,7)

def find2sum(lst):
    start,end = 0,len(lst)-1
    while start<end:
        sum_ = lst[start]+lst[end]
        if sum_ < x:
            start = start + 1
        elif sum_ > x:
            end = end - 1
        else:
            return (lst[start], lst[end])
    return -1

lst = [1,2,3,5,6,7]
print lst
x = int(input())
print find2sum(lst)
