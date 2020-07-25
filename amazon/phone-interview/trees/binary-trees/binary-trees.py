class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.visited = False

def height_(node, prevDepth, maxDepth):
    if node is None:
        print(maxDepth)
        return
    currentDepth = prevDepth+1
    maxDepth = max(maxDepth, currentDepth)
    height_(node.left, currentDepth, maxDepth)
    height_(node.right, currentDepth, maxDepth)

def printPaths(node, paths):
    if node is None:
        return
    print(node.value)
    paths.append(node.value)
    if node.left is not None and node.right is not None:
        print(paths)
    printPaths(node.left, paths)
    printPaths(node.right, paths)
    paths.pop()

def isBalancedBTree(node):
    if node is None:
        return True
    else:
        lDepth = height(node.left)
        rDepth = height(node.right)
    if abs(lDepth-rDepth) <= 1:
        return True
    else:
        return False

def height(node):
    if node is None:
        return 0
    else:
        lDepth = height(node.left)
        rDepth = height(node.right)
        maxDepth = max(lDepth, rDepth)
        return maxDepth+1

def inOrderTraverse(node):
    if node is None:
        return
    inOrderTraverse(node.left)
    print(node.value)
    inOrderTraverse(node.right)

def preOrderTraverse(node):
    if node is None:
        return
    print(node.value)
    preOrderTraverse(node.left)
    preOrderTraverse(node.right)

def postOrderTraverse(node):
    if node is None:
        return
    postOrderTraverse(node.left)
    postOrderTraverse(node.right)
    print(node.value)

def inOrderTraverseUsingStack(node):
    stack = []
    stack.append(node)
    while len(stack) >= 0:
        node = stack.pop()
        if node.visited:
            print(node.value)
        else:
            node.visited = True
            if node.left is not None: stack.append(node.left)
            if node is not None: stack.append(node)
            if node.right is not None: stack.append(node.right)

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(9)
    root.right = Node(11)
    root.left.left = Node(8)
    root.right.right = Node(12)
    print("Max Depth of Tree: ",height(root))
    maxDepth = 0
    height_(root,0,maxDepth)
    print("Max Depth of Tree: ",maxDepth)
    print(" >> In-Order Traversal ")
    inOrderTraverse(root)
    print(" >> Pre-Order Traversal ")
    preOrderTraverse(root)
    print(" >> Post-Order Traversal ")
    postOrderTraverse(root)
    print(" ==== ")
    printPaths(root, [])
