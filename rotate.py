from array import array

def rotate(arr, d):
    for i in range(0,d):
        arr.append(arr[0])
        arr.pop(0)
    return arr

def cyclic_rotate(arr, d):
    for i in range(0,d):
        arr.insert(0,arr[-1])
        arr.pop()
    return arr

if __name__ == "__main__":
    a = array('i',[1,2,3,4,5,6,7])
    print rotate(a,2)
    print cyclic_rotate(a,2)
