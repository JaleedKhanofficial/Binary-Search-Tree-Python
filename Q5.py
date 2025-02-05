# Step 5
# Inside the __init__ method, initialize the left and right attributes of the node to None. This is because when a node is first created, it doesn't have any left or right children. Remember to use the self keyword.


class TreeNode:    
    def __init__(self, key):
        self.key = key
        self.left = None                    # step 5
        self.right = None                   # step 5