'''Write a program to create a class/structure TreeNode to represent a node in a binary search tree. Each node  should have three attributes: data, left, and right. Then, create a class/structure BinaryTree to  represent the binary tree itself. Implement the following operations: 
1. in_order_traversal(): Perform an in-order traversal of the tree and print the data of each node. 
2. post_order_traversal(): Perform a post-order traversal of the tree and print the data of each node.'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert a new node into the binary search tree."""
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

    def in_order_traversal(self):
        """Perform in-order traversal and print the data of each node."""
        self._in_order_recursive(self.root)

    def _in_order_recursive(self, node):
        if node is not None:
            self._in_order_recursive(node.left)
            print(node.data, end=" ")
            self._in_order_recursive(node.right)

    def post_order_traversal(self):
        """Perform post-order traversal and print the data of each node."""
        self._post_order_recursive(self.root)

    def _post_order_recursive(self, node):
        if node is not None:
            self._post_order_recursive(node.left)
            self._post_order_recursive(node.right)
            print(node.data, end=" ")


# Example usage
tree = BinaryTree()
elements = [50, 30, 70, 20, 40, 60, 80]
for elem in elements:
    tree.insert(elem)

print("In-order Traversal:")
tree.in_order_traversal()
print("\nPost-order Traversal:")
tree.post_order_traversal()
