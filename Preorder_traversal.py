class TreeNode:
    def __init__(self, value):
        # Initialize a tree node with a value
        self.value = value
        self.left = None  # Left child of the node
        self.right = None  # Right child of the node

def preorder_traversal(root):
    """
    Performs a preorder traversal of a binary tree.
    Preorder traversal visits nodes in the order: Root, Left, Right.
    """
    # Base case: If the node is None, return an empty list (no more nodes to visit)
    if root is None:
        return []
    
    # Process the root node
    # The current node is added to the result list before its children
    root_value = [root.value]
    
    # Recursively traverse the left subtree
    # Preorder traversal processes the left subtree after the root node
    left_values = preorder_traversal(root.left)
    
    # Recursively traverse the right subtree
    # Preorder traversal processes the right subtree after the left subtree
    right_values = preorder_traversal(root.right)
    
    # Combine root, left subtree, and right subtree values to return the complete preorder traversal
    return root_value + left_values + right_values

# Example Usage:
# Constructing a binary tree for demonstration
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)

# Perform preorder traversal
result = preorder_traversal(root)

# Output:
# The preorder traversal of the tree will visit nodes in the order: 1, 2, 4, 5, 3, 7
print(result)  # Output: [1, 2, 4, 5, 3, 7]

# Key Notes:
# 1. Preorder traversal visits nodes in the order: Root -> Left subtree -> Right subtree.
# 2. In this traversal, the root node is visited before its children.
# 3. The algorithm is typically implemented using recursion for simplicity.
# 4. Time Complexity: O(n) - Every node is visited exactly once.
# 5. Space Complexity: O(h) - The recursion stack depth is proportional to the height of the tree (h).
