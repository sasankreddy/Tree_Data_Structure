class BST:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        """
        Find the kth largest element in a Binary Search Tree (BST) using reverse inorder traversal.
        
        Approach:
        - Reverse inorder traversal of a BST gives elements in descending order.
        - We traverse the tree in reverse inorder and keep a counter to track the kth element.
        - Once we reach the kth element, we return it.
        
        Time Complexity: O(n), where n is the number of nodes in the tree, as we may need to visit all nodes in the worst case.
        Space Complexity: O(h), where h is the height of the tree due to the recursion stack.
        """
        # Helper function to perform reverse inorder traversal
        def reverse_inorder(node: TreeNode) -> int:
            if not node or self.count >= k:
                return []
            # Traverse the right subtree, then visit the node, then traverse the left subtree
            return reverse_inorder(node.right) + [node.val] + reverse_inorder(node.left)

        self.count = 0  # Initialize the counter for kth largest element
        
        # Perform reverse inorder traversal and return the kth largest element
        reverse_inorder_list = reverse_inorder(root)
        return reverse_inorder_list[k - 1]  # Return kth largest element (0-indexed list)
