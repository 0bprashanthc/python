def max_index(arr):
    max_ind = -1
    for i in range(0,len(arr)):
        for j in range(len(arr)-1,i,-1):
            if arr[i] <= arr[j]:
                diff = j - i
                break
        if diff > max_ind:
            max_ind = diff
        diff = 0
    return max_ind

if __name__ == "__main__":
    arr = [34,8,10,3,2,80,30,33,1]
    print(max_index(arr))
