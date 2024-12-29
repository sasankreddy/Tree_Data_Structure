#Leet code 515 - Medium
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        Finds the largest value in each row of a binary tree.
        
        Approach:
        - We perform a **level-order traversal (BFS)** using a queue to traverse the tree level by level.
        - For each level, we find the maximum value and add it to the result list.
        - We use a queue to process nodes in a level-wise manner, ensuring all nodes in each row are processed before moving to the next row.
        
        Time Complexity: O(n) - Every node is visited once during the level-order traversal.
        Space Complexity: O(n) - The space required by the queue is proportional to the number of nodes at the widest level of the tree.
        """
        res = []  # List to store the largest value at each level
        queue = deque([root])  # Initialize the queue with the root node
        
        while queue:
            levelvalues = []  # Temporary list to store the values at the current level
            
            for i in range(len(queue)):
                node = queue.popleft()  # Dequeue a node
                
                if node:
                    levelvalues.append(node.val)  # Add the node's value to the list
                    queue.append(node.left)  # Add the left child to the queue
                    queue.append(node.right)  # Add the right child to the queue
            
            if levelvalues:
                res.append(max(levelvalues))  # Add the max value of the current level to the result list
        
        return res  # Return the list of largest values for each row


# Time Complexity: O(n)
# - Every node in the tree is visited once during the level-order traversal.
# - n is the total number of nodes in the tree.

# Space Complexity: O(n)
# - The queue may store all nodes at the widest level of the tree, which can be O(n) in the worst case (for example, in a fully populated binary tree).
