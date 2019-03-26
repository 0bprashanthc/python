"""
Given a list of stock prices for a company, 
find the maximum amount of money you could have 
made with one trade (one buy/sell). 
For example, if A = [2,3,1,4,5,7,5,4], 
the max money with a single trade is 6, 
if you buy at 1 and sell at 7.
"""
a = [2,3,1,4,5,7,5,4]
a = [8,14,2,5,7,3,9,5]
min_so_far,max_diff = None, 0
for index,value in enumerate(a):
    if min_so_far is None:
        min_so_far = value
    elif min_so_far > value:
        min_so_far = value
    max_diff = max(max_diff, value-min_so_far)
print max_diff
