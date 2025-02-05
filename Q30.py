# Step 30
# Note that, your search returns something like 80: <__main__.TreeNode object at 0x108b3e0>. This is the default string representation when printing an instance of a class.

# To change that to print a useful value, define another method named __str__ in the TreeNode class. It takes a single argument self.

# After defining __str__ you'll get an exception in the console because the __str__ method doesn't return anything yet. You'll work on the method body in the next step.


class TreeNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):              # step 30
        pass                        # step 30

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:

            node.right = self._insert(node.right, key)
        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)
        
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    
    def search(self, key):
        return self._search(self.root, key)

bst = BinarySearchTree()

nodes = [50, 30, 20, 40, 70, 60, 80]

for node in nodes:
    bst.insert(node)

print('Search for 80:', bst.search(80))
