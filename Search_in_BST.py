#Leet Code 700- Easy 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Searches for a node in a binary tree with a given value.
        
        Approach:
        - We perform a **breadth-first search (BFS)** to traverse the tree level by level.
        - We use a queue to store nodes, starting with the root node.
        - For each node, we check if it matches the given value.
        - If the value is found, return the node.
        - If not, we add the left and right children to the queue if they exist and continue the search.
        
        Time Complexity: O(n) - In the worst case, we may need to visit all nodes.
        Space Complexity: O(n) - In the worst case, the queue may store all nodes, especially for a tree that is very wide.
        """
        if root is None:
            return None  # If the tree is empty, return None
        
        queue = [root]  # Initialize queue with the root node
        
        # Perform BFS to find the target node
        while queue:
            temp = queue.pop(0)  # Dequeue a node
            
            if temp.val == val:
                return temp  # If node is found, return the node
            
            # Add left child to the queue if it exists
            if temp.left is not None and temp.left not in queue:
                queue.append(temp.left)
            
            # Add right child to the queue if it exists
            if temp.right is not None and temp.right not in queue:
                queue.append(temp.right)
        
        return None  # If node with the given value is not found


# Time Complexity: O(n)
# - We may visit all nodes in the worst case when the value is not present in the tree or when the tree is unbalanced.
# - n is the number of nodes in the tree.

# Space Complexity: O(n)
# - In the worst case, the queue may store all nodes at the same level, especially for a wide tree.
# - The space complexity is proportional to the maximum number of nodes at any level in the tree.
