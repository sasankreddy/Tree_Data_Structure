# Leetcode 102 - Easy
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        Checks if a binary tree is symmetric (a mirror of itself).
        
        My Approach:
        - A tree is symmetric if its left subtree is a mirror reflection of its right subtree.
        - We perform a recursive check using a helper function `is_mirror` to compare left and right subtrees.
        - The `is_mirror` function compares:
            1. If both nodes are None, they are mirrors.
            2. If one node is None and the other is not, they are not mirrors.
            3. If the node values are different, they are not mirrors.
            4. Recursively check the left and right subtrees for mirror symmetry.
        """
        
        if not root:
            return True  # An empty tree is symmetric by definition
        
        def is_mirror(left: TreeNode, right: TreeNode) -> bool:
            # Base case: If both nodes are None, they are mirrors
            if not left and not right:
                return True
            # If one node is None and the other is not, they are not mirrors
            if not left or not right:
                return False
            # If values are different, they are not mirrors
            if left.val != right.val:
                return False
            # Recursively check the left and right subtrees
            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
        
        # Start the recursive comparison of the left and right subtrees
        return is_mirror(root.left, root.right)
