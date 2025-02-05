# Step 18
# Now, inside the insert method, you need to call the helper method _insert() that we defined earlier. Here, _insert has encapsulated the implementation of the insertion logic. This is useful for recursion and for keeping the implementation details hidden from the user.

# Delete pass and assign self._insert(self.root, key) to self.root.

# Note that:

# self.root passes the root node of the tree as the first argument. This is the starting point for the insertion process.
# key: passes the key value you want to insert as the second argument.

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
        self.root =self._insert(self.root, key)                 # step 18