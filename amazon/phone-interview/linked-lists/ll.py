class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node
        return self.next

class LinkedList(object):
    def __init__(self, head=None, length=1):
        self.head = head
        self.length = length

    def get_length(self):
        return self.length

    def get_node(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                return node
            node = node.next
        return None

    def get_head(self):
        return self.head
    
    def set_head(self, node):
        self.head = node

    def insert_beginning(self, data):
        if data is None:
            return None
        node = Node(data=data, next_node=self.head)
        self.set_head(node)
        self.length += 1

    def insert_end(self, data):
        if data is None:
            return None
        node = Node(data=data)
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = node
        self.length += 1

    def insert_after(self, data, new_data):
        n = self.head
        while n is not None:
            if n.data == data:
                node = Node(data=new_data,next_node=n.next)
                n.set_next(node)
            n = n.next

if __name__ == "__main__":
    first_node = Node(data=1)
    llist = LinkedList(first_node)
    llist.insert_beginning(2)
    llist.insert_end(3)
    llist.insert_after(data=1,new_data=21)
    node = llist.get_head()
    while node is not None:
        print(node, node.data, node.next)
        node = node.next
    del first_node
    del llist
