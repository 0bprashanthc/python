def binary_search(lst, number):
    #implements binary search
    lower, upper = 0, len(lst)-1
    mid = (lower+upper)//2
    found = False
    while lower <= upper:
        if number > lst[mid]:
            lower = mid +1
        elif number < lst[mid]:
            upper = mid-1
        elif number == lst[mid]:
            found = True
            break
        mid = (lower+upper)//2
    return mid if found else -1

def rotate_search(a, k):
    value = -1
    first, second = a[:a.index(max(a))],a[a.index(max(a))+1:]
    if k == max(a):
        value = a.index(max(a))
    else:
        if k > first[0]:
            value = search(first, k)
        else:
            value = search(second, k)+1
            value += a.index(max(a))
    return value

def sum_search(a, s):
    first, second = a[:a.index(max(a))],a[a.index(max(a))+1:]

if __name__ == "__main__":
    a = [11, 15, 6, 8, 9, 10]
    print a
    number = int(raw_input("Enter number to search: "))
    print rotate_search(a,number)
