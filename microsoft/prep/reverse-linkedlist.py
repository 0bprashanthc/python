"""
Given a linked list of N nodes. The task is to reverse this list.

Input: Head of following linked list
1->2->3->4->NULL
Output: Linked list should be changed to,
4->3->2->1->NULL
"""
class Node():
    def __init__(self,data):
        self.data = data
        self.next = data

def reverse(node):
    _prev,_next,current = None,None,node
    while current is not None:
        _next = current.next
        current.next = _prev
        _prev = current
        current = _next
