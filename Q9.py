# Step 9
# Next, you need to define a mechanism to insert nodes in the tree. For that, you need to define an _insert method, which is a helper function and would be used by the actual insert method later on.

# This method is recursive, meaning it calls itself to traverse the tree until the appropriate location for the new node is found.

# Define an _insert method with the parameters self, node and key.


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert(self, node, key):                   # step 9
        pass                                        # step 9 