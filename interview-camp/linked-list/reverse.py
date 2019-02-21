#reverse a linked list with O(1) space
from LinkedList import *

head = Node(1)
node = append(head,2)
node = append(node,3)
node = append(node,4)
node = append(node,5)
node = append(node,6)
node = append(node,7)
node = append(node,8)
prev, current = None, head
print "*************"
while current.next is not None:
    print current.data, current.next
    current = current.next
print current.data, current.next
current = head
while current.next is not None:
    node = current.next
    current.next = prev
    prev = current
    current = node
current.next = prev
prev = current
print "**** REVERSE ****"
while prev.next is not None:
    print prev.data, prev.next
    prev = prev.next
print prev.data, prev.next
