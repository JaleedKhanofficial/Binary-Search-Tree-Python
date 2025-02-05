# Step 11
# Now you need to recursively traverse the tree and insert the values using the principle for binary trees:

# Values smaller than the key are placed in the left subtree
# Values greater than the key are placed in the right subtree
# After your existing conditional statement, write another if statement to check if key is less than node.key.

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

        if key < node.key:                          # step 11
            pass                                    # step 11