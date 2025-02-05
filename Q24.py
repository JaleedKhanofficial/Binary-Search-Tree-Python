# Step 24
# Inside the search method, delete pass and call the helper method _search with the following arguments.

# self.root: This is the root of the binary search tree. The search starts from the root.
# key: This is the value that the user wants to find in the binary search tree.
# Internally, search delegates the actual search logic to the _search helper method that performs the actual recursive search within the binary search tree.


class TreeNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


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
        self._search(self.root, key)                    # step 24