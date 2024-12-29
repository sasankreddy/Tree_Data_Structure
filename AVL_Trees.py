class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 1  # Height of node (initially 1)

class AVLTree:
    def insert(self, root, val):
        # 1. Perform normal BST insertion
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        
        # 2. Update the height of this ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
        # 3. Get the balance factor
        balance = self.getBalance(root)
        
        # 4. If this node becomes unbalanced, then there are 4 cases
        
        # Left Left Case
        if balance > 1 and val < root.left.val:
            return self.rightRotate(root)
        
        # Right Right Case
        if balance < -1 and val > root.right.val:
            return self.leftRotate(root)
        
        # Left Right Case
        if balance > 1 and val > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        # Right Left Case
        if balance < -1 and val < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        
        # Perform rotation
        y.left = z
        z.right = T2
        
        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        
        # Perform rotation
        y.right = z
        z.left = T3
        
        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        
        return y
    
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):
        if not root:
            return []
        return [root.val] + self.preOrder(root.left) + self.preOrder(root.right)

# Example usage
avl = AVLTree()
root = None
values = [10, 20, 30, 25, 28, 5, 4]

# Inserting values one by one and displaying the tree after each insertion

for val in values:
    root = avl.insert(root, val)
    print(f"Tree after inserting {val}: {avl.preOrder(root)}")
    
    # Step-by-step tree representation in comments:
    
    # After inserting 10:
    #      10
    # The tree is just the root node with a height of 1.

    # After inserting 20:
    #      10
    #        \
    #         20
    # The tree is still balanced with no need for rotation.

    # After inserting 30:
    #      10
    #        \
    #         20
    #           \
    #            30
    # The tree becomes unbalanced with a balance factor of -2 at root (10), triggering a left rotation.
    # After left rotation on 10:
    #       20
    #      /  \
    #    10    30
    # The tree is now balanced again.

    # After inserting 25:
    #       20
    #      /  \
    #    10    30
    #         /
    #        25
    # The tree is balanced with no need for rotation.

    # After inserting 28:
    #       20
    #      /  \
    #    10    30
    #         /
    #        25
    #          \
    #           28
    # The tree becomes unbalanced with a balance factor of 2 at node (30), requiring a right-left rotation.
    # After right rotation on 25:
    #       20
    #      /  \
    #    10    30
    #         /
    #        28
    #       /
    #      25
    # After left rotation on 30:
    #       20
    #      /  \
    #    10    28
    #         /  \
    #        25   30
    # The tree is now balanced again.

    # After inserting 5:
    #       20
    #      /  \
    #    10    28
    #   /  \   /  \
    #  5   25  30
    # The tree remains balanced.

    # After inserting 4:
    #       20
    #      /  \
    #    10    28
    #   /  \   /  \
    #  5   25  30
    # /
    #4
    # The tree becomes unbalanced with a balance factor of 2 at node (10), triggering a right rotation.
    # After right rotation on 10:
    #       20
    #      /  \
    #    5     28
    #   / \    /  \
    #  4  10  25  30
    # The tree is balanced again.

# Final AVL Tree:
#       20
#      /  \
#    5     28
#   / \    /  \
#  4  10  25  30

# Pre-order Traversal:
# [20, 5, 4, 10, 25, 28, 30]
