# Step 20
# Now you are going to define a base case for the recursive search. Remove the current pass and write an if statement that checks two conditions:

# If node is None: This indicates that the search has reached the end of a branch without finding the key.
# If node.key == key: This means that the key has been found in the current node.
# Combine the two conditions with the or operator and return the current node inside the if block.


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
        if node is None or node.key == key:                             # step 20
            return node                                                 # step 20