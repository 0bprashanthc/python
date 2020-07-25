def beginning(arr):
    boundary = 0
    for i in range(0,len(arr)):
        if arr[i] == 0:
            arr[i],arr[boundary] = arr[boundary],arr[i]
            boundary += 1

if __name__ == "__main__":
    arr = [4,0,2,0,1,0,3,0]
    print(arr)
    beginning(arr)
    print(arr)
