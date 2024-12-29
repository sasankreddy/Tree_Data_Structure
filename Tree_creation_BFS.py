from collections import deque  # Import deque for efficient queue operations

class TreeNode:
    def __init__(self, value):
        # Initialize a tree node with a value
        self.value = value
        self.left = None  # Left child of the node
        self.right = None  # Right child of the node

def create_tree_bfs(values):
    """
    Creates a binary tree using BFS (Level-Order Traversal) from a list of values.
    Null/None represents missing nodes.
    """
    # BFS uses a queue to process nodes level by level, ensuring we explore nodes in breadth-first order.
    if not values:
        return None
    
    root = TreeNode(values[0])  # Root node created first
    queue = deque([root])  # Initialize the queue with the root node
    index = 1  # Start from the second element in the values list
    
    # Process nodes until the queue is empty
    while queue and index < len(values):
        current_node = queue.popleft()  # Remove the front node from the queue
        
        # Check if left child should be added
        if values[index] is not None:
            current_node.left = TreeNode(values[index])  # Create left child
            queue.append(current_node.left)  # Add left child to the queue
        index += 1
        
        # Check if right child should be added
        if index < len(values) and values[index] is not None:
            current_node.right = TreeNode(values[index])  # Create right child
            queue.append(current_node.right)  # Add right child to the queue
        index += 1
    
    # Return the constructed tree
    return root

# Example Usage:
# Input: List of values in level-order (None represents missing nodes)
values = [1, 2, 3, 4, 5, None, 7]

# Build the tree using BFS
root = create_tree_bfs(values)

# The constructed tree:
#        1
#      /   \
#     2     3
#    / \      \
#   4   5      7

# Key Notes:
# 1. BFS uses a queue to explore nodes level by level, ensuring that we process nodes in breadth-first order.
# 2. The algorithm starts with the root node, then adds its children to the queue, and proceeds to the next level.
# 3. BFS ensures that nodes are visited in the order they appear in a level-order traversal.
# 4. Time Complexity: O(n) - Each node is processed once.
# 5. Space Complexity: O(n) - The queue can store all nodes at a given level, which is proportional to the number of nodes.
