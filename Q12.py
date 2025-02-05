# Step 12
# If key < node.key evaluates to True, then the new node should be placed in the left subtree.

# Delete pass and recursively call the _insert method with left child as the first argument and key as the second argument. Assign the result to the left attribute of the current node.

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
            node.left = self._insert(node.left, key)                        # step 12