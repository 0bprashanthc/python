def dutch_sort(arr,pivot):
    low, high = 0, len(arr)-1
    i = 0
    while i <= high:
        if arr[i] < pivot:
            arr[i],arr[low] = arr[low],arr[i]
            low += 1
            i += 1
        elif arr[i] > pivot:
            arr[i],arr[high] = arr[high],arr[i]
            high -= 1
        else:
            i +=1

if __name__ == "__main__":
    arr = [5,2,4,4,6,4,4,3]
    arr = [1,0,1,2,1,0,1,2]
    print(arr)
    dutch_sort(arr,1)
    print(arr)
