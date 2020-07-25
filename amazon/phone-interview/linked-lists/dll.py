class Node(object):
    def __init__(self, data=None, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def get_prev(self):
        return self.prev_node

    def get_next(self):
        return self.next_node

    def get_data(self):
        return self.data

    def set_prev(self, node):
        self.prev_node = node

    def set_next(self, node):
        self.next_node = node

    def set_data(self, data):
        self.data = data

class DoubleLinkedList(object):
    def __init__(self, head, length=1):
        self.head = head
        self.length = length
    
    def get_head(self):
        return self.head

    def get_length(self):
        return self.length

    def insert_beginning(self, data):
        n = self.head
        node = Node(data=data)
        node.set_next(self.head)
        n.set_prev(node)
        self.head = node
        self.length += 1

    def insert_end(self, data):
        n = self.head
        node = Node(data=data)
        while n is not None:
            if n.next_node is None:
                n.set_next(node)
                node.set_prev(n)
                self.length += 1
                break
            n = n.next_node

    def insert_after(self, new_data, data):
        n = self.head
        while n is not None:
            if n.data == data:
                break
            n = n.next_node
        node = Node(data=new_data,prev_node=n,next_node=n.next_node)
        n.next_node.set_prev(node)
        n.set_next(node)
        self.length += 1

    def get_data(self, data):
        n = self.head
        while n is not None:
            if n.data == data:
                return n
        return None

if __name__ == "__main__":
    head = Node(1)
    dll = DoubleLinkedList(head)
    dll.insert_end(2)
    dll.insert_beginning(3)
    dll.insert_after(4,3)
    n = dll.get_head()
    while n is not None:
        print(n, n.data, n.prev_node, n.next_node)
        n = n.next_node
    del dll
    del head
