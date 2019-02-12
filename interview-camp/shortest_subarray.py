def shortest_subarray(lst):
    print lst
    i,j = None, None
    #traverse from beginning for i
    for index,value in enumerate(lst):
        if value > lst[index+1]:
            i = index
            break
    print i
    #traverse from end for j
    index = len(lst)-1
    while index >= 0:
        if lst[index] < lst[index-1]:
            j = index
            break
        index = index - 1
    print j
    if i is not None and j is not None:
        subarray = lst[i:j+1]
        print i,j,subarray
        min_, max_ = min(subarray), max(subarray)
        index = 0
        while index != i:
            if lst[index] > min_:
                i = index
                break
            index = index + 1
        print i
        index = len(lst)-1
        while index != j:
            if lst[index] < max_:
                j = index
                break
            index = index - 1
        return lst[i:j+1]

if __name__ == "__main__":
    lst = [1,3,5,2,6,4,7,8,9]
    #lst = [1,2,4,5,3,5,6,7,9]
    #lst = [0,2,5,3,1,8,6,9]
    print shortest_subarray(lst)
