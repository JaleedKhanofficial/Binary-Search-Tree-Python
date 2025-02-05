# Step 22
# If the second if statement is not True, it means that the target key is greater than or equal to the current node key.

# In a binary search tree, if the target key is greater than the current node's key, the search continues in the right subtree.

# After the if block, return the result of calling the _search method with the right child of the current node and the key as arguments.


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
        
        return self._search(node.right, key)                    # step 22