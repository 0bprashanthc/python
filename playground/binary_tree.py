from tree import Node

if __name__ == "__main__":
    root = Node(10)
    root.add(7)
    root.add(11)
    print root.exists(int(input()))
