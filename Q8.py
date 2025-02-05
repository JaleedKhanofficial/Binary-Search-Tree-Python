# Step 8
# Inside the __init__ method, delete pass and initialize root to the value None.

# The root attribute represents the root node of the binary search tree. Since this is the constructor when a new BinarySearchTree object is created, it starts with an empty tree, so the root attribute is set to None.

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None                    # step 8
        