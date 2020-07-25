"""
array = [] #path
len = 0
node
if node is not None
   push node to array
   len += 1
if node is None #leaf 
   print the array
else
   recurse node.left, array, len
   recurse node.right, array, len
"""
def print_paths(arr,node):
    if node is None:
        print(arr)
        return
    arr.append(node.data)
    print_paths(arr, node.left)
    print_paths(arr, node.right)
    arr.pop()


