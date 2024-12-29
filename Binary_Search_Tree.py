# Definition for a binary tree node.
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Converts a sorted array to a balanced binary search tree (BST).
        
        Approach:
        - The middle element of the sorted array will be the root of the tree to ensure balanced depth.
        - The left half of the array will form the left subtree, and the right half will form the right subtree.
        - This approach ensures the tree is balanced, as the middle element of the array minimizes the height difference between subtrees.
        
        Returns the root of the balanced BST.
        """
        if not nums:
            return None  # Base case: if the array is empty, return None
        
        mid = len(nums) // 2  # Find the middle element of the array
        root = TreeNode(nums[mid])  # Create the root node with the middle element
        
        # Recursively build the left subtree with the left half of the array
        root.left = self.sortedArrayToBST(nums[:mid])
        
        # Recursively build the right subtree with the right half of the array
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root  # Return the root of the balanced BST


# Time Complexity: O(n) 
# - Every element in the array is processed once during the recursive calls.

# Space Complexity: O(log n)
# - The recursion stack depth is proportional to the height of the tree, which is log(n) for a balanced tree.
