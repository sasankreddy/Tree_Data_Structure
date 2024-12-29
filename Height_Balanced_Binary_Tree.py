#Leetcode 110 EASY
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Checks if a binary tree is balanced. A binary tree is balanced if, 
        for every node, the height difference between its left and right subtrees 
        is at most 1.
        
        Approach:
        - A recursive helper function `heightcheck` is used to calculate the height 
          of each subtree and check whether the tree is balanced at each node.
        - The height of a subtree is defined as the maximum depth from the node to its 
          farthest leaf.
        - If any subtree is unbalanced (i.e., the height difference between left and 
          right child exceeds 1), the function returns `False`.
        - The base case for recursion is when the node is `None`, in which case the 
          tree is balanced with a height of 0.
        
        Time Complexity: O(n) - Each node is visited once to compute the height and balance.
        Space Complexity: O(h) - The recursion depth is proportional to the height of the tree (h).
        """
        def heightcheck(node):
            if not node:
                return [True, 0]  # The tree is balanced with height 0 for null nodes
            
            left = heightcheck(node.left)  # Check left subtree
            right = heightcheck(node.right)  # Check right subtree
            
            # A tree is balanced if both subtrees are balanced and the height difference is <= 1
            balance = (left[0] and right[0]) and abs(left[1] - right[1]) <= 1
            return [balance, 1 + max(left[1], right[1])]  # Return balance status and height
        
        return heightcheck(root)[0]  # Return whether the tree is balanced


# Time Complexity: O(n)
# - We visit every node once to compute the height and balance of the tree.
# - n is the number of nodes in the tree.

# Space Complexity: O(h)
# - The space used by the recursion stack is proportional to the height of the tree (h).
# - In the worst case (unbalanced tree), the height could be O(n), where n is the number of nodes.
# - In the best case (balanced tree), the height is O(log n).
