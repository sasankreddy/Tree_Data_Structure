#Leet code 112 - EASY# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Determines if the binary tree has a root-to-leaf path such that the sum of the node values
        along the path equals the targetSum.
        
        Approach:
        - A recursive DFS approach is used to traverse the tree from the root to the leaves.
        - At each node, we subtract the node's value from the target sum, and check if either the 
          left or right subtree can complete the sum.
        - If a leaf node is reached and the remaining sum is zero, the path is valid, and we return `True`.
        - If the node is `None`, the path does not exist, and we return `False`.
        
        Time Complexity: O(n) - We visit every node once.
        Space Complexity: O(h) - The space used by the recursion stack, where h is the height of the tree.
        """
        if root is None:
            return False  # If the tree is empty, there's no path

        if root.left is None and root.right is None:
            # If it's a leaf node, check if the remaining sum equals the node's value
            return root.val == targetSum

        remainingsum = targetSum - root.val  # Subtract the node's value from the target sum
        
        # Recursively check the left and right subtrees
        return (self.hasPathSum(root.left, remainingsum) or self.hasPathSum(root.right, remainingsum))


# Time Complexity: O(n)
# - We visit every node in the tree once to check for the path sum.
# - n is the number of nodes in the tree.

# Space Complexity: O(h)
# - The space used by the recursion stack is proportional to the height of the tree (h).
# - In the worst case (unbalanced tree), the height could be O(n), and in the best case (balanced tree), it is O(log n).
