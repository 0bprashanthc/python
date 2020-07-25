"""
Given two linked lists sorted in increasing order. Merge them such a way that
the result list is in decreasing order (reverse order).
"""
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

def merge(node1,node2):
    node3 = Node(None)
    node3 = merge(node1,node2)
