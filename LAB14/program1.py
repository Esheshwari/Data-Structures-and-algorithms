'''Write a program to create a class/structure TreeNode to represent a node in a binary search tree. Each node  should have three attributes: data, left, and right. Then, create a class/structure BinaryTree to  represent the binary tree itself. Implement the following operations: 
1. .insert(data): Insert a new node with the given data into the binary tree (assume a simple insertion  without balancing). 
2. .pre_order_traversal(): Perform a pre-order traversal of the tree and print the data of each node. '''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)

    def pre_order_traversal(self):
        self._pre_order_recursive(self.root)

    def _pre_order_recursive(self, node):
        if node is not None:
            print(node.data, end=" ")
            self._pre_order_recursive(node.left)
            self._pre_order_recursive(node.right)

# Example usage:
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(18)

print("Pre-order Traversal:")
tree.pre_order_traversal()
