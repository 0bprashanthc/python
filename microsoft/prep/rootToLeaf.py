class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def rootToLeafSum(node,sum_):
    if node is None:
        return sum_==0
    else:
        ans = 0
        subSum = (sum_)-(node.data)
        if (subSum==0) and (node.left is None) and (node.right is None):
            return True
        if node.left is not None:
            ans = ans or rootToLeafSum(node.left,subSum)
        if node.right is not None:
            ans = ans or rootToLeafSum(node.right,subSum)
    return ans
