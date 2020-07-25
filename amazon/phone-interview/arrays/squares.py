def squares(arr):
    result = [None]*len(arr)
    i,j,end = 0,len(arr)-1,len(arr)-1
    while i<=j:
        if abs(arr[i]) > abs(arr[j]):
            result[end] = arr[i]*arr[i]
            i += 1
        else:
            result[end] = arr[j]*arr[j]
            j -= 1
        end -= 1
    return result

if __name__ == "__main__":
    arr = [-4,-2,-1,0,3,5] 
    print(arr)
    print(squares(arr))
