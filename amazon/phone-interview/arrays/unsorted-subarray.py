def unsorted(arr):
    i,j = 0, len(arr)-1
    start,end = -1,-1
    while i <= j:
        if start != -1 and end != -1:
            break
        if arr[i] > arr[i+1]:
            start = i
        if arr[j] < arr[j-1]:
            end = j
        i += 1
        j -= 1
    print(start,end)
    sub = arr[start:end+1]
    print(sub)
    min_arr, max_arr = min(sub),max(sub)
    for i in arr[:start]:
        if i > min_arr:
            start = arr.index(i)
    for i in arr[end:]:
        if i < max_arr:
            end = arr.index(i)
    return arr[start: end+1]

if __name__ == "__main__":
    arr = [0,2,3,1,8,6,9]
    arr = [1,2,4,5,3,5,6,7]
    arr = [1,3,5,2,6,4,7,8,9]
    print(arr)
    print(unsorted(arr))
