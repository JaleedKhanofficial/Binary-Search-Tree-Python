# Step 51
# Replace pass with an if statement that checks if the current node (node) is not empty. Then, recursively call _inorder_traversal with node.left and result as the arguments.


class TreeNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)

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
        return self._search(node.right, key)
    
    def search(self, key):
        return self._search(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key) 
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left   
            
            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)   
        
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.key

    def _inorder_traversal(self, node, result):
        if node:                                                                # step 51
            node.left = self._inorder_traversal(node.left, result)              # step 51

bst = BinarySearchTree()

nodes = [50, 30, 20, 40, 70, 60, 80]

for node in nodes:
    bst.insert(node)

# print('Search for 80:', bst.search(80))