from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        """
        Checks if a binary tree is a complete binary tree.
        
        Approach:
        - A binary tree is complete if all levels are filled except possibly the last, 
          and all nodes are as left as possible.
        - We perform a level-order traversal (BFS) using a queue to traverse the tree.
        - If we encounter a null (None) node, all subsequent nodes must also be null for the tree to be complete.
        
        Time Complexity: O(n) - We visit each node once during the level-order traversal.
        Space Complexity: O(n) - The queue holds nodes, and in the worst case (when the tree is a perfect binary tree), 
                               it will hold up to n nodes.
        """
        q = deque([root])  # Queue to perform level-order traversal
        size = 0  # Count the number of nodes visited
        
        while q:
            node = q.popleft()
            if node:
                size += 1  # If the node is not null, increment the node count
                q.append(node.left)
                q.append(node.right)
            else:
                # Once a null node is encountered, all subsequent nodes must be null
                while q:
                    if q.popleft():  # If any non-null node is encountered after a null node, it's not complete
                        return False
        return True  # If no non-null nodes were found after a null, the tree is complete
