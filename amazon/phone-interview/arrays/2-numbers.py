def twoNumbersSum(arr, x):
    i,j = 0, len(arr)-1
    while i < j:
        count = arr[i]+arr[j]
        if count > x:
            j -= 1
        elif  count < x:
            i += 1
        else:
            return (arr[i],arr[j])
    return (-1,-1)

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    arr = [1,2,3,5,6,7]
    x = 9
    x = 11
    print(twoNumbersSum(arr,x))
