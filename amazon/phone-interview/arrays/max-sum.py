def max_sum(arr):
    if max(arr) < 0:
        return max(arr)
    max_sofar, max_tillnow = arr[0],arr[0]
    for i in range(1,len(arr)):
        max_tillnow += arr[i]
        max_tillnow = max(max_tillnow,arr[i])
        max_sofar = max(max_sofar, max_tillnow)
    return max_sofar

if __name__ == "__main__":
    arr =  [1,2,-1,2,-3,2,-5]
    print(arr)
    print(max_sum(arr))
