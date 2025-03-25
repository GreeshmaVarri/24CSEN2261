#blackbox ai 
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_rec(node.right, key)

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search_rec(node.left, key)
        return self._search_rec(node.right, key)

    def inorder_traversal(self):
        return self._inorder_rec(self.root)

    def _inorder_rec(self, node):
        return self._inorder_rec(node.left) + [node.val] + self._inorder_rec(node.right) if node else []

# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    print("Inorder Traversal:", bst.inorder_traversal())  # Output: [2, 3, 4, 5, 7]
    print("Search for 4:", bst.search(4) is not None)  # Output: True
