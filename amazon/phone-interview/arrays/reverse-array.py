def reverse(arr):
    i,j = 0,len(arr)-1
    while i < j:
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1

if __name__ == "__main__":
    arr = [3,5,2,5,2,3,9]
    arr = [1,2,3,4,5,6]
    print(arr)
    reverse(arr)
    print(arr)
