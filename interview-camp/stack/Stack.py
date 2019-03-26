class StackNode(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def push(newNode, top):
    top.next = newNode
    return newNode

def pop(top):
    top = prev
    return prev

def peek():
    return top
