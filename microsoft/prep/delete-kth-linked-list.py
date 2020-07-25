"""
Given a singly linked list, Your task is to remove every K-th node of the
linked list. Assume that K is always less than or equal to length of Linked
List.
"""
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

def delete_kth(node,k):
    count,_prev = 0,None
    while node is not None:
       _prev = node
       count += 1
       if count==k:
           delete_node(_prev,node)
           count = 0
       node = node.next

def delete_node(prev,node):
    prev.next = node.next
    del node
