def sort(arr):
    for i in range(0,len(arr)):
        min_sofar = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_sofar]:
                min_sofar = j
        arr[i],arr[min_sofar] = arr[min_sofar],arr[i]

if __name__ == "__main__":
    arr = [2,7,4,1,5,3]
    arr = [122,11,34,1,65,78,90]
    print(arr)
    sort(arr)
    print(arr)
