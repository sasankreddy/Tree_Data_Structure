#Inserstion to BST
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def insert(self, root: TreeNode, val: int) -> TreeNode:
        """
        Inserts a new value into the BST, maintaining the binary search property.
        
        Key Points:
        - If the tree is empty, the new value becomes the root.
        - Otherwise, the value is inserted in the correct position, based on comparison:
          - Values smaller than the current node go to the left subtree.
          - Values larger go to the right subtree.
        - The process is recursive, comparing the value at each node until we find the correct position.

        Time Complexity: O(h), where h is the height of the tree (O(log n) for balanced BST, O(n) for unbalanced).
        Space Complexity: O(h), due to recursion stack space.
        """
        if root is None:
            return TreeNode(val)  # If root is None, return a new TreeNode with the value
        
        if val < root.val:
            # If the value is smaller, insert it into the left subtree
            root.left = self.insert(root.left, val)
        else:
            # If the value is larger, insert it into the right subtree
            root.right = self.insert(root.right, val)
        
        return root  # Return the root after insertion

#2. Delete node in binary search tree
class BST:
    def delete(self, root: TreeNode, val: int) -> TreeNode:
        """
        Deletes a node with a specific value from the BST.
        
        Key Points:
        - If the node has no children or only one child, replace it with its child.
        - If the node has two children, find its inorder successor (the smallest value in the right subtree), 
          replace the node with the successor's value, and delete the successor.
        - The process is recursive, finding the node to delete and performing the necessary operations.

        Time Complexity: O(h), where h is the height of the tree (O(log n) for balanced BST, O(n) for unbalanced).
        Space Complexity: O(h), for recursive calls.
        """
        if not root:
            return root  # If the tree is empty, return None
        
        # Find the node to delete
        if val < root.val:
            root.left = self.delete(root.left, val)  # Recur on the left subtree
        elif val > root.val:
            root.right = self.delete(root.right, val)  # Recur on the right subtree
        else:
            # Case 1: Node with one child or no child
            if not root.left:
                return root.right  # Replace the node with its right child
            elif not root.right:
                return root.left  # Replace the node with its left child
            
            # Case 2: Node with two children
            # Find the inorder successor (the smallest value in the right subtree)
            min_larger_node = self._min_value_node(root.right)
            root.val = min_larger_node.val  # Replace node's value with the inorder successor's value
            root.right = self.delete(root.right, min_larger_node.val)  # Delete the inorder successor

        return root  # Return the root after deletion

    def _min_value_node(self, node: TreeNode) -> TreeNode:
        """
        Finds the node with the smallest value in a given subtree (leftmost node).
        """
        current = node
        while current.left:
            current = current.left  # Keep going left until the leftmost node is found
        return current  # Return the leftmost node
#3. Search element in Binary Search Tree
class BST:
    def search(self, root: TreeNode, val: int) -> TreeNode:
        """
        Searches for a value in the BST and returns the node containing that value.
        
        Key Points:
        - The search is performed by comparing the value to be searched with the current node's value.
        - If the value is smaller, search the left subtree; if larger, search the right subtree.
        - The search continues recursively until the value is found or the subtree is empty.
        
        Time Complexity: O(h), where h is the height of the tree (O(log n) for balanced BST, O(n) for unbalanced).
        Space Complexity: O(h), for recursive calls.
        """
        if not root or root.val == val:
            return root  # If the root is None or the value is found, return the root
        
        if val < root.val:
            return self.search(root.left, val)  # If value is smaller, search left subtree
        return self.search(root.right, val)  # If value is larger, search right subtree
'''
Time and Space Complexity Summary:
Insertion:

Time Complexity: O(h), where h is the height of the tree.
Space Complexity: O(h) due to the recursive call stack.
Deletion:

Time Complexity: O(h), where h is the height of the tree.
Space Complexity: O(h), for recursion stack space.
Search:

Time Complexity: O(h), where h is the height of the tree.
Space Complexity: O(h), for recursion stack space.
In a balanced BST, h is O(log n), and in the worst case (unbalanced tree), h could be O(n).
'''