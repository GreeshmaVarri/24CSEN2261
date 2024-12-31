#BLACKBOX AI 
def linear_search(arr, target):
    """Search for a target number in the array using linear search."""
    for index in range(len(arr)):
        if arr[index] == target:
            return index  # Return the index of the found element
    return -1  # Return -1 if the element is not found

def add_element(arr, element):
    """Add an element to the end of the array."""
    arr.append(element)
    return arr

def remove_element(arr, target):
    """Remove the first occurrence of the target number from the array."""
    try:
        arr.remove(target)  # Remove the first occurrence of the target
    except ValueError:
        print(f"Element {target} not found in the array.")
    return arr

# Example usage
array = [5, 3, 8, 6, 2]

# Adding an element
new_element = 10
print(f"Array before adding: {array}")
array = add_element(array, new_element)
print(f"Array after adding {new_element}: {array}")

# Searching for an element
target_number = 6
result = linear_search(array, target_number)
if result != -1:
    print(f"Number {target_number} found at index: {result}")
else:
    print(f"Number {target_number} not found in the array.")

# Removing an element
element_to_remove = 3
print(f"Array before removing {element_to_remove}: {array}")
array = remove_element(array, element_to_remove)
print(f"Array after removing {element_to_remove}: {array}")

# Trying to remove an element that doesn't exist
element_to_remove = 15
array = remove_element(array, element_to_remove

OUTPUT : 
Array before adding: [5, 3, 8, 6, 2]
Array after adding 10: [5, 3, 8, 6, 2, 10]
Number 6 found at index: 3
Array before removing 3: [5, 3, 8, 6, 2, 10]
Array after removing 3: [5, 8, 6, 2, 10]
Element 15 not found in the array.
