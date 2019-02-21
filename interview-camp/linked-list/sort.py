#input: 1,0,2,0,1,0,2,1
#output: 0,0,0,1,1,1,2,2
from LinkedList import *

if __name__ == "__main__":
    head = Node(1)
    node = head
    node = append(node, 1)
    node = append(node, 1)
    node = append(node, 2)
    node = append(node, 2)
    node = append(node, 2)
    node = append(node, 1)
    node = append(node, 2)
    node = append(node, 2)
    node = append(node, 1)
    head_0 = Node()
    head_1 = Node()
    head_2 = Node()
    node = head
    node_0 = head_0
    node_1 = head_1
    node_2 = head_2
    for i in range(8):
        print node.data
        if node.data == 0:
            node_0 = append(node_0, node.data)
        elif node.data == 1:
            node_1 = append(node_1, node.data)
        elif node.data == 2:
            node_2 = append(node_2, node.data)
        node = node.next
    node_0.next = head_1
    node_1.next = head_2
    node = head_0
    print "===== AFTER SORT ====="
    for i in range(8):
        print node.data
        node = node.next
