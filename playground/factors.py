#!/usr/bin/env python
# *-* coding: utf-8 *-*
import sys
import time
start_time = time.time()

def factorset(number):
    factors = set()
    for i in range(1,int(number)):
        quotient, remainder = divmod(number, i)
        if remainder == 0:
            if (i not in factors) or (quotient not in factors):
                factors.add(i)
                factors.add(quotient)
    return factors

def factorlist(number):
    factors = []
    for i in range(1, number):
        quotient, remainder = divmod(number, i)
        if remainder == 0:
            if (i not in factors) or (quotient not in factors):
                factors.append(i)
                factors.append(quotient)
    return factors

if __name__ == "__main__":
    number = int(sys.argv[1])
    #print factorset(number)
    print factorlist(number)
    print("--- %s seconds ---" % (time.time() - start_time))
