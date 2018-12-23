class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add(self,data):
        if self.data:
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.add(data)
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.add(data)

    def tree(self):
        if self.left:
            self.left.tree()
        if self.right:
            self.right.tree()
        print self.data

    def exists(self,data):
        if self.data == data:
            return True
        if data < self.data:
            if self.left is not None:
                return self.left.exists(data)
        if data > self.data:
            if self.right is not None:
                return self.right.exists(data)
        return False
