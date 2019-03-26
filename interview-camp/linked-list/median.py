#given a linked list with no cycle, find its median
from LinkedList import *

head = Node(1)
node = append(head,2)
third = append(node,3)
node = append(third,4)
node = append(node,5)
node = append(node,6)
node = append(node,7)
x = head
for i in range(7):
    print x, x.data, x.next
    x = x.next
slow,fast = head,head
while fast.next is not None:
    fast = fast.next
    fast = fast.next
    slow = slow.next
print "=== MEDIAN ==="
print slow, slow.data, slow.next
