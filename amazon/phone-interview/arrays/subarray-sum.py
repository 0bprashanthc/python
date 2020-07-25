def subarray(arr,s):
    sum_tillnow = arr[0]
    start = 0
    for i in range(1,len(arr)):
        sum_tillnow += arr[i]
        if sum_tillnow > s:
            sum_tillnow -= arr[start]
            start += 1
        if sum_tillnow == s:
            return (start,i)
    return -1

if __name__ == "__main__":
    arr = [1,2,3,7,5]
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    print(subarray(arr,23))
