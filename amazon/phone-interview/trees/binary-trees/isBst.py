def isbst(root):
    if root is None:
        return True
    if isSubTreeLesserThan(root.left, root.value) \
            and isSubTreeGreaterThan(root.right, root.value) \
            and isbst(root.left) and isbst(root.right):
                return True
    return False
