class Node:
    data, next = None, None  
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def append(node, data):
    if node.data is None:
        node.data = data
        return node
    else:
        new_node = Node(data)
        node.next = new_node
        return new_node

if __name__ == "__main__":
    #input: 1,0,2,0,1,0,2,1
    #output: 0,0,0,1,1,1,2,2
    head = Node(0)
    node = Node(1)
    head.next = node
    for i in range(2,10):
        node = append(node, i)
    node = head
    for i in range(0,10):
        print node, node.data, node.next
        node = node.next
