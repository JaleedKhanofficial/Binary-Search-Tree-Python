# Step 19
# It's time to work on the search functionality. Just like you created a helper method _insert for the insert method, you need to create a helper method _search for the search method.

# Define the _search method with three parameters, namely self,node and key.


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

    def _search(self, node, key):                   # step 19
        pass                                        # step 19
