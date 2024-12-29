class TreeNode:
    def __init__(self, value):
        # Initialize a tree node with a value
        self.value = value
        self.left = None  # Left child of the node
        self.right = None  # Right child of the node

def create_tree_dfs(values, index=0):
    """
    Creates a binary tree using DFS from a list of values (level-order traversal).
    Null/None represents missing nodes.
    """
    # Depth-First Search (DFS) uses a recursive approach to process each node and its children.
    # Each recursive call processes one node and links it to its left and right subtrees.
    
    # Base case: If index is out of bounds or value is None, return None
    if index >= len(values) or values[index] is None:
        return None
    
    # Create a new tree node with the current value
    root = TreeNode(values[index])
    
    # Recursively construct the left subtree
    # The left child is at index 2 * index + 1 in a level-order traversal
    root.left = create_tree_dfs(values, 2 * index + 1)
    
    # Recursively construct the right subtree
    # The right child is at index 2 * index + 2 in a level-order traversal
    root.right = create_tree_dfs(values, 2 * index + 2)
    
    # Return the constructed tree node
    return root

# Example Usage:
# Input: List of values in level-order (None represents missing nodes)
values = [1, 2, 3, 4, 5, None, 7]

# Build the tree using DFS
root = create_tree_dfs(values)

# The constructed tree:
#        1
#      /   \
#     2     3
#    / \      \
#   4   5      7

# Key Notes:
# 1. DFS is naturally implemented with recursion, traversing as far as possible before backtracking.
# 2. The recursive approach simplifies tree construction by handling nodes and their children in separate calls.
# 3. Time Complexity: O(n) - Processes each node once.
# 4. Space Complexity: O(h) - Uses stack space proportional to the tree's height (h).
