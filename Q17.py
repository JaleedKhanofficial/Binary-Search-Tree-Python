# Step 17
# The insert method will be called by the user. In addition to the self parameter, it will also need a key parameter. This parameter will be the key value to insert into the binary search tree.

# Add key as the second parameter to the function definition.

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

    def insert(self, key):                  # step 17
        pass