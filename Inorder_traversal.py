class TreeNode:
    def __init__(self, value):
        # Initialize a tree node with a value
        self.value = value
        self.left = None  # Left child of the node
        self.right = None  # Right child of the node

def inorder_traversal(root):
    """
    Performs an inorder traversal of a binary tree.
    Inorder traversal visits nodes in the order: Left, Root, Right.
    """
    # Base case: If the node is None, return an empty list (no more nodes to visit)
    if root is None:
        return []
    
    # Recursively traverse the left subtree
    # Inorder traversal processes the left subtree first
    left_values = inorder_traversal(root.left)
    
    # Process the root node
    # After visiting the left child, the current node is added to the result list
    root_value = [root.value]
    
    # Recursively traverse the right subtree
    # After the current node, the right subtree is processed
    right_values = inorder_traversal(root.right)
    
    # Combine left subtree, root, and right subtree values to return the complete inorder traversal
    return left_values + root_value + right_values

# Example Usage:
# Constructing a binary tree for demonstration
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)

# Perform inorder traversal
result = inorder_traversal(root)

# Output:
# The inorder traversal of the tree will visit nodes in the order: 4, 2, 5, 1, 3, 7
print(result)  # Output: [4, 2, 5, 1, 3, 7]

# Key Notes:
# 1. Inorder traversal visits nodes in the order: 

#                     Left subtree -> Root node -> Right subtree.

# 2. In a binary search tree (BST), the inorder traversal produces a sorted sequence of node values.
# 3. The algorithm is typically implemented using recursion, making it a simple and intuitive approach.
# 4. Time Complexity: O(n) - Every node is visited exactly once.
# 5. Space Complexity: O(h) - The recursion stack depth is proportional to the height of the tree (h).
