def reverse(a):
    a = a.split()
    i = len(a)-1
    result = ""
    while i >= 0:
        result += a[i]+" "
        i -= 1
    print result

if __name__ == "__main__":
    #"i live in a house" = "house a in live i"
    a = " qqq"
    print a
    reverse(a)
