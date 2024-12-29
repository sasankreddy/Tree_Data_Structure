class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Find the Lowest Common Ancestor (LCA) of two nodes in a Binary Search Tree (BST).
        
        Approach:
        - The BST property ensures that nodes in the left subtree are smaller, and nodes in the right subtree are larger than the root.
        - We compare the values of p and q with the root.
        - If both p and q are smaller than the root, then LCA must be in the left subtree.
        - If both p and q are larger than the root, then LCA must be in the right subtree.
        - If p and q lie on different sides of the root, the root is the LCA.
        
        Time Complexity: O(h), where h is the height of the tree. In the worst case, we may need to traverse the entire height of the tree.
        Space Complexity: O(1), as we are using only a constant amount of extra space for the variables.
        """
        # Traverse the tree starting from the root
        while root:
            if p.val < root.val and q.val < root.val:
                # Both p and q are smaller than root, move to the left subtree
                root = root.left
            elif p.val > root.val and q.val > root.val:
                # Both p and q are larger than root, move to the right subtree
                root = root.right
            else:
                # One node is on the left and the other is on the right (or one of them is the root)
                # This means we have found the LCA
                return root
        return None  # If no LCA is found (not possible in a valid BST with valid nodes)
