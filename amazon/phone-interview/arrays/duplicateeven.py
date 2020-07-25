#[1,2,5,6,8] 

def duplicateEven(arr):
    count = evens(arr)
    i = len(arr)-1
    arr.extend([None]*count)
    j = i + count
    while i >=0:
        if arr[i]%2 == 0:
            arr[j],arr[j-1] = arr[i],arr[i]
            j -= 2
        else:
            arr[j] = arr[i]
            j -= 1
        i -= 1

def evens(arr):
    count = 0
    for i in range(0,len(arr)):
        if i % 2 == 0:
            count += 1
    return count

if __name__ == "__main__":
    arr = [1,2,5,6,8] 
    print(arr)
    duplicateEven(arr)
    print(arr)
