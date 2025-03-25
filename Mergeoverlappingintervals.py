#chatgpt ai 
def merge_intervals(intervals):
    """
    Function to merge overlapping intervals.
    
    Args:
        intervals (list of lists): List of intervals where each interval is represented as [start, end].
        
    Returns:
        list: Merged list of intervals without overlap.
    """
    if not intervals:
        return []
    
    # Step 1: Sort the intervals by the start time
    intervals.sort(key=lambda x: x[0])
    
    # Step 2: Initialize the merged intervals list with the first interval
    merged = [intervals[0]]
    
    # Step 3: Iterate through the sorted intervals and merge where necessary
    for current in intervals[1:]:
        # Get the last merged interval
        last_merged = merged[-1]
        
        # If the current interval overlaps with the last merged one, merge them
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])  # Merge by updating the end time
        else:
            # Otherwise, add the current interval to the merged list
            merged.append(current)
    
    return merged

# Example usage:
intervals = [[1, 3], [2, 4], [5, 7], [6, 8], [9, 10]]
merged_intervals = merge_intervals(intervals)
print(f"Merged intervals: {merged_intervals}")
