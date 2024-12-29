class Solution:
    def heapify(self, arr, n, i):
        """
        Helper function to maintain the heap property.
        This function ensures that the subtree rooted at index 'i' follows the heap property.
        
        Time Complexity: O(log n) - In the worst case, the element needs to be pushed down to the leaf level.
        """
        largest = i  # Initialize largest as root
        left = 2 * i + 1  # Left child index
        right = 2 * i + 2  # Right child index

        # If left child is larger than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # If right child is larger than largest so far
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is not root, swap and continue heapifying the affected subtree
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap
            self.heapify(arr, n, largest)  # Recursively heapify the affected subtree

    def heapSort(self, arr):
        """
        Main function to perform Heap Sort.
        
        Approach:
        - Build a max-heap from the input array.
        - Swap the root (largest element) with the last element.
        - Reduce the heap size and heapify the root again to maintain the heap property.
        - Repeat the process for all elements until the heap size is 1.
        
        Time Complexity: O(n log n) - Building the heap takes O(n), and extracting elements takes O(log n) for each element.
        Space Complexity: O(1) - No additional space is used except for the input array.
        """
        n = len(arr)

        # Build a max heap
        # Start from the last non-leaf node and heapify each node
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # Extract elements one by one from the heap
        for i in range(n - 1, 0, -1):
            # Move the current root to the end of the array
            arr[i], arr[0] = arr[0], arr[i]
            # Call heapify on the reduced heap
            self.heapify(arr, i, 0)

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
solution = Solution()
solution.heapSort(arr)
print("Sorted array is:", arr)
