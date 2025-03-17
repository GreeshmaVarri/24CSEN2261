#CHATGPT AI
class Node:
    """A class representing a single node in the linked list."""
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node, initially set to None

class LinkedList:
    """A class representing the linked list."""
    def __init__(self):
        self.head = None  # Head of the list, initially set to None
    
    def append(self, data):
        """Appends a new node with given data to the end of the list."""
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty
            self.head = new_node
            return
        last = self.head
        while last.next:  # Traverse to the last node
            last = last.next
        last.next = new_node  # Set the next of the last node to the new node
    
    def prepend(self, data):
        """Prepend a new node with given data to the start of the list."""
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Make new node point to current head
        self.head = new_node  # Update head to the new node
    
    def delete(self, key):
        """Delete the first node with the given data (key)."""
        current = self.head
        if current is not None:
            if current.data == key:  # If the head node needs to be deleted
                self.head = current.next  # Move head to the next node
                current = None  # Free memory
                return
        # Traverse to find the node to delete
        while current is not None:
            if current.data == key:
                break
            prev = current
            current = current.next
        # If the node was not found
        if current is None:
            print("Node with data {} not found.".format(key))
            return
        prev.next = current.next  # Skip over the node to delete it
        current = None  # Free memory
    
    def print_list(self):
        """Prints the elements of the linked list."""
        current = self.head
        if current is None:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Indicate end of list
    
    def search(self, key):
        """Searches for a node with the given data (key)."""
        current = self.head
        while current:
            if current.data == key:
                return True  # Node found
            current = current.next
        return False  # Node not found

# Example usage
if __name__ == "__main__":
    ll = LinkedList()

    # Append nodes to the linked list
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)

    # Print the list
    print("Initial List:")
    ll.print_list()

    # Prepend a node
    ll.prepend(5)
    print("\nAfter Prepending 5:")
    ll.print_list()

    # Delete a node
    ll.delete(20)
    print("\nAfter Deleting 20:")
    ll.print_list()

    # Search for a node
    found = ll.search(30)
    print(f"\nSearch for 30: {'Found' if found else 'Not Found'}")

    ll.delete(100)
