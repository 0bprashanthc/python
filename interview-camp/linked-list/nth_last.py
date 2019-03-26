#given a linked list, find nth last element of the linked list
from LinkedList import *

head = Node(1)
node = append(head,2)
third = append(node,3)
node = append(third,4)
node = append(node,5)
node = append(node,6)
node = append(node,7)
node = append(node,8)
n = int(input("n : "))
x = head
while x.next is not None:
    print x, x.data, x.next
    x = x.next
if n < 8:
    p1,p2,count = head,head,0
    while count != n:
        p2 = p2.next
        count = count + 1
    while p2.next is not None:
        p2 = p2.next
        p1 = p1.next
    print "=== Nth last element ==="
    print p1, p1.data 
else:
    print -1
