#deleting a node from linked list
#input: 32,41,9, delete = 41
#output: 32,9
from LinkedList import *

head = Node()
node = append(head, 32)
node = append(node, 41)
node = append(node, 9)
x = head
delete = 41
prev = x
for i in range(3):
    if x.data == delete:
        prev.next = x.next
    prev = x
    x = x.next
x = head
for i in range(3):
    if x is not None:
        print x.data, x.next
        x = x.next
    
