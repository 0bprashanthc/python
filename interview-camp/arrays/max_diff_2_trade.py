"""
Given a list of stock prices for a company, 
find the maximum amount of money you could have 
made with two trades (two buy/sell)
For example, if A = [2,3,1,4,5,7,5,4], 
"""
a = [2,3,1,4,5,7,5,4]
min_so_far,max_so_far = None,None
max_diff_1,max_diff_2 = 0,0
max_diff_start, max_diff_end = {},{}
for index,value in enumerate(a):
    if (min_so_far is None) or (min_so_far > value):
        min_so_far = value
    max_diff_1 = max(max_diff_1,value-min_so_far)
    max_diff_start[index] = max_diff_1
print max_diff_start
i = len(a)-1
while i >=0:
    if (max_so_far is None) or (max_so_far < a[i]):
        max_so_far = a[i]
    max_diff_2 = max(max_diff_2, max_so_far-a[i])
    max_diff_end[i] = max_diff_2
    i = i - 1
print max_diff_end
max_2_trades = 0
for index,value in enumerate(a):
    max_2_trades = max(max_2_trades,max_diff_start[index]+max_diff_end[index])
print "==== MAX MONEY WITH 2 TRADES ===="
print max_2_trades
