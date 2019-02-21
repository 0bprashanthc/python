#given a linked list, find cycle in the linked list
#if cycle is observed in the linked list, 
#   give the length of the cycle
from LinkedList import *

head = Node(1)
node = append(head,2)
third = append(node,3)
node = append(third,4)
node = append(node,5)
node = append(node,6)
node = append(node,7)
node = append(node,8)
node.next = third
x = head
for i in range(10):
    print x, x.data, x.next
    x = x.next
slow,fast,cycle = head,head,None
isCyclic = False
while fast.next is not None:
    fast = fast.next
    if slow==fast:
        isCyclic = True
        print fast.data
        break
    fast = fast.next
    if slow==fast:
        isCyclic = True
        print fast.data
        break
    slow = slow.next
print isCyclic,fast
cycle,count = fast.next,1
while cycle != fast:
    count = count + 1
    print cycle.data,cycle.next
    cycle = cycle.next
print "count: "+str(count)

