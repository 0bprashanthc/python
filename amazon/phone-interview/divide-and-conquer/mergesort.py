count = 0
def sort(arr, low, high):
    global count 
    if low < high:
        mid = (low+(high-1))/2
        sort(arr, low, mid)
        sort(arr, mid+1, high)
        count = count + merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    c = 0
    n1, n2 = (mid-low+1),(high-mid)
    L, R = [0]*n1, [0]*n2
    for i in range(0,n1):
        L[i] = arr[i + low]
    for j in range(0,n2):
        R[j] = arr[j + mid+1]
    i,j,k = 0,0,low
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            c += 1
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    return (c)

if __name__ == "__main__":
    arr = [122,11,34,1,65,78,90]
    arr = [1, 20, 6, 4, 5] 
    print(arr)
    sort(arr, 0, len(arr)-1)
    print(arr)
    print(count)
