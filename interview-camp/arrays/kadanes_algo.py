a = [1,2,-1,2,-3,2,-5]
a = [-2,-3,4,-1,-2,1,5,-1]

"""
sf, eh = 0,0
0: eh = max(0,0+1) = 1, sf = max(0,1) = 1
1: eh = max(0,1+2) = 3, sf = max(1,3) = 3
2: eh = max(0,3-1) = 2, sf = max(3,2) = 3
3: eh = max(0,2+2) = 4, sf = max(3,4) = 4
4: eh = max(0,4-3) = 1, sf = max(4,1) = 4
5: eh = max(0,1+2) = 3, sf = max(4,3) = 4
6: eh = max(0,3-5) = -2,sf = max(4,-2)= 4
===========================================
sf, eh = 0,0
0: eh = max(0,0-2) = 0, sf = max(0,0) = 0
1: eh = max(0,0-3) = 0, sf = max(0,0) = 0
2: eh = max(0,0+4) = 4, sf = max(0,4) = 4
3: eh = max(0,4-1) = 3, sf = max(4,3) = 4
4: eh = max(0,3-2) = 1, sf = max(4,1) = 4
5: eh = max(0,1+1) = 2, sf = max(4,2) = 4
6: eh = max(0,2+5) = 7, sf = max(4,7) = 7
7: eh = max(0,7-1) = 6, sf = max(7,6) = 7
-2:0 -5:1 -1:2 -2:3 -4:4 -3:5 1:6 0:7
===========================================
sf, eh = 0,0
for i in range(0,len(a)):
    eh = max(0, eh+a[i])
    sf = max(sf,eh)
print sf
curr_sum = 0
for i in range(0,len(a)):
    curr_sum = curr_sum + a[i]
    _map[curr_sum] = i
    if curr_sum == sf:
        print 0,i
    if curr_sum-sf in _map.keys():
        print _map[curr_sum-sf],i
print None
"""

"""
#solution 1
max_so_far, max_end_here = 0,0
for i in range(0,len(a)):
    max_end_here = a[i]
    if max_end_here < 0:
        max_end_here = 0
    if max_so_far < max_end_here:
        max_so_far = max_end_here
print max_so_far
"""

#solution 2
max_so_far, max_end_here = a[0],a[0]
for i in range(1,len(a)):
    max_end_here = max(0,max_end_here+a[i])
    max_so_far = max(max_so_far, max_end_here)
print max_so_far
print a
curr_sum = 0
_map = {}
for i in range(len(a)):
    curr_sum = curr_sum + a[i]
    if curr_sum == max_so_far:
        print 0,i
        break
    if curr_sum-max_so_far in _map:
        print _map[curr_sum-max_so_far]+1,i
        break
    _map[curr_sum] = i
    print _map

