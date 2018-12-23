a = [5, 6, 7, 8, 9, 10, 1, 2, 3]

def binary(a, k):
    first, second = a[:a.index(max(a))],a[a.index(max(a))+1:]
    if k < max(first):
        print binary_search(first, k)
    if k < max(second):
        print binary_search(first, k)

