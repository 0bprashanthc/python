def prime_sieving(n):
    primes = [True for i in range(n+1)]
    p = 2
    while p*p <= n:
        if primes[p]:
            for i in range(p*p,n,p):
                primes[i] = False
        p += 1
    for i in range(2,n):
        if primes[i]:
            print(i)

if __name__ == "__main__":
    n = 30
    prime_sieving(n)
