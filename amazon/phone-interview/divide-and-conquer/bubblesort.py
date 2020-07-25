def sort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

if __name__ == "__main__":
    arr = [122,11,34,1,65,78,90]
    print(arr)
    sort(arr)
    print(arr)
