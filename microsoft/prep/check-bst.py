"""
Given a binary tree, return true if it is BST, else false. For example, the
following tree is not BST, because 11 is in left subtree of 10. The task is to
complete the function isBST() which takes one argument, root of Binary Tree.
"""
def isBST(node,left,right):
    if node is None:
        return True
    if (left is not None) and (left.data >= node.data):
        return False
    if (right is not None) and (right.data <= node.data):
        return False
    return isBST(node.left,left,node.data) and
isBST(node.right,node.data,right)
