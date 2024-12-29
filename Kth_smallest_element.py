class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Find the kth smallest element in a Binary Search Tree (BST) using inorder traversal.
        
        Approach:
        - Inorder traversal of a BST gives elements in ascending order.
        - We traverse the tree in inorder and keep a counter to track the kth element.
        - Once we reach the kth element, we return it.
        
        Time Complexity: O(n), where n is the number of nodes in the tree, as we may need to visit all nodes in the worst case.
        Space Complexity: O(h), where h is the height of the tree due to the recursion stack.
        """
        # Helper function to perform inorder traversal
        def inorder(node: TreeNode) -> int:
            if not node:
                return []
            # Traverse the left subtree, then visit the node, then traverse the right subtree
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        # Perform inorder traversal and return the kth smallest element (1-based index)
        inorder_list = inorder(root)
        return inorder_list[k - 1]  # Return kth smallest element (0-indexed list)

