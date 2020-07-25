# you can write to stderr for debugging purposes, e.g.
# sys.stderr.write("this is a debug message\n")
import sys

def solution(N):
    # write your code in Python 3.6
    def isDivisiblebyAll(i):
        if isDivisiblebyThree(i) and str(i)[-1]=="0":
            return True
        return False
    
    def isDivisiblebyTwoThree(i):
        if i % 6 == 0:
            return True
        return False
    
    def isDivisiblebyTwoFive(i):
        if str(i)[-1] == "0":
            return True
        return False
    
    def isDivisiblebyThreeFive(i):
        if isDivisiblebyThree(i) and isDivisiblebyFive(i):
            return True
        return False
    
    def isDivisiblebyTwo(i):
        if i % 2 == 0:
            return True
        return False
    
    def isDivisiblebyThree(i):
        if i % 3 == 0:
            return True
        return False
    
    def isDivisiblebyFive(i):
        if i % 5 == 0:
            return True
        return False
    
    for i in range(1,N+1):
        if isDivisiblebyAll(i):
            sys.stdout.write("CodilityTestCoders\n")
        elif isDivisiblebyTwoThree(i):
            sys.stdout.write("CodilityTest\n")
        elif isDivisiblebyTwoFive(i):
            sys.stdout.write("CodilityCoders\n")
        elif isDivisiblebyThreeFive(i):
            sys.stdout.write("TestCoders\n")
        elif isDivisiblebyTwo(i):
            sys.stdout.write("Codility\n")
        elif isDivisiblebyThree(i):
            sys.stdout.write("Test\n")
        elif isDivisiblebyFive(i):
            sys.stdout.write("Coders\n")
        else:
            sys.stdout.write(str(i)+"\n")

