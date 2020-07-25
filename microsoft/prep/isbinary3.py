"""
Given a binary number, write a program that prints 1 if given binary number is
a multiple of 3.  Else prints 0. The given number can be big upto 2^100. It is
recommended to finish the task using one traversal of input binary string.
"""
def isbinary3(num):
    odd_count,even_count = 0,0
    for i in range(0,len(num)):
        if num[i]=='1':
            if i%2==0:
                even_count += 1
            else:
                odd_count += 1
    if abs(odd_count-even_count)%3==0:
        return True
