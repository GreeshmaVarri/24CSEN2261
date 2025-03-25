#chatgpt ai 
import heapq

def find_kth_largest(nums, k):
    """
    Function to find the kth largest element in an unsorted array.
    
    Args:
        nums (list): A list of integers.
        k (int): The rank (kth) of the largest element to find.
    
    Returns:
        int: The kth largest element in the list.
    """
    if not nums or k <= 0 or k > len(nums):
        raise ValueError("Invalid input. Make sure k is between 1 and the length of the list.")
    
    # Initialize a min-heap with the first k elements of nums
    min_heap = nums[:k]
    heapq.heapify(min_heap)  # Turn the list into a heap
    
    # For each remaining element, if it is larger than the smallest in the heap, replace it
    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappushpop(min_heap, num)  # Push the current element and pop the smallest
    
    # The root of the heap is the kth largest element
    return min_heap[0]

# Example usage:
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(f"The {k}th largest element is: {find_kth_largest(nums, k)}")
