def rotate(arr):
    start,end = 0, len(arr)-1
    i = 0
    while start+i < end:
        tmp = arr[start][start+i]
        arr[start][start+i] = arr[end-i][start]
        arr[end-i][start] = arr[end][end-i]
        arr[end][end-i] = arr[start+i][end]
        arr[start+i][end] = tmp
        i += 1
        start += 1

if __name__ == "__main__":
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    for i in arr:
        print(i)
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
    for i in range(0,len(arr)):
        start,end = 0,len(arr[i])-1
        while start < end:
            arr[i][start],arr[i][end] = arr[i][end],arr[i][start]
            start += 1
            end -= 1
    for i in arr:
        print(i)
