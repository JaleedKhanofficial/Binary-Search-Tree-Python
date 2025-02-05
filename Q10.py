# Step 10
# Now you need to check if the node parameter is None. If it is, this means that the method has reached a leaf node or an empty spot in the tree where the new node should be inserted.

# Inside the _insert method body, replace pass with an if statement that checks if node is None.

# Inside the new if block, return TreeNode(key) to create a new TreeNode instance with the provided key. This will become the new leaf node, effectively inserting the key into the tree.

class TreeNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def _insert(self, node, key):
        if node is None:                            # step 10
            return TreeNode(key)                    # step 10