def gcd(a,b):
    if a < b:
        if a == 0:
            return b
        return gcd(b%a,a)
    if b == 0:
        return a
    return gcd(a%b,b)

if __name__ == "__main__":
    print(gcd(10,15))
