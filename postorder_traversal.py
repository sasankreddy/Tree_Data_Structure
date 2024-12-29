class TreeNode:
    def __init__(self, value):
        # Initialize a tree node with a value
        self.value = value
        self.left = None  # Left child of the node
        self.right = None  # Right child of the node

def postorder_traversal(root):
    """
    Performs a postorder traversal of a binary tree.
    Postorder traversal visits nodes in the order: Left, Right, Root.
    """
    # Base case: If the node is None, return an empty list (no more nodes to visit)
    if root is None:
        return []
    
    # Recursively traverse the left subtree
    # Postorder traversal processes the left subtree first
    left_values = postorder_traversal(root.left)
    
    # Recursively traverse the right subtree
    # Postorder traversal processes the right subtree after the left subtree
    right_values = postorder_traversal(root.right)
    
    # Process the root node
    # After visiting both left and right subtrees, the current node is added to the result list
    root_value = [root.value]
    
    # Combine left subtree, right subtree, and root values to return the complete postorder traversal
    return left_values + right_values + root_value

# Example Usage:
# Constructing a binary tree for demonstration
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)

# Perform postorder traversal
result = postorder_traversal(root)

# Output:
# The postorder traversal of the tree will visit nodes in the order: 4, 5, 2, 7, 3, 1
print(result)  # Output: [4, 5, 2, 7, 3, 1]

# Key Notes:
# 1. Postorder traversal visits nodes in the order: Left subtree -> Right subtree -> Root.
# 2. The algorithm ensures that children are processed before their parent node.
# 3. This is useful in scenarios where we need to process children before parents (e.g., deleting nodes).
# 4. Time Complexity: O(n) - Every node is visited exactly once.
# 5. Space Complexity: O(h) - The recursion stack depth is proportional to the height of the tree (h).
