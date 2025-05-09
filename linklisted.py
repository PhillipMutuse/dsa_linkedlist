class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(node):
    while node:
        print(f"{node.data} -> ", end="")
        node = node.next
    print("null")

# Create nodes
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

print_list(node1)
