"""
Given a singly linked list of N nodes. The task is to find middle of the linked
list. For example, if given linked list is 1->2->3->4->5 then output should be
3.
If there are even nodes, then there would be two middle nodes, we need to print
second middle element. For example, if given linked list is 1->2->3->4->5->6
then output should be 4.
"""
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

def middle(node):
    slow,fast = None,None
    while fast is not None:
        slow = slow.next
        fast = fast.next
        fast = fast.next
    return slow.data
