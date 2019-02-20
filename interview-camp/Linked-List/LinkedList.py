class Node:
    data, next = None, None  
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

head = Node(0)
node = Node(1)
head.next = node
for i in range(22,30):
    new_node = Node(i)
    node.next = new_node
    node = new_node

node = head
for i in range(0,10):
    print node, node.data, node.next
    node = node.next
