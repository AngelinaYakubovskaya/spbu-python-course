import random
from collections.abc import MutableMapping


class TreeNode:
    """A node in the Cartesian tree."""

    def __init__(self, key, value):
        """Initialize a tree node with a key, value, and a random priority."""
        self.key = key
        self.value = value
        self.priority = random.random()  # Random priority for heap property
        self.left = None
        self.right = None


class CartesianTree(MutableMapping):
    """A Cartesian Tree that implements MutableMapping."""

    def __init__(self):
        """Initialize an empty Cartesian tree."""
        self.root = None
        self.size = 0

    def split(self, node, key):
        """Split the tree rooted at node into two trees around key."""
        if node is None:
            return None, None

        if key < node.key:
            left, node.left = self.split(node.left, key)
            return left, node
        else:
            node.right, right = self.split(node.right, key)
            return node, right

    def merge(self, left, right):
        """Merge two trees left and right into a single tree."""
        if left is None:
            return right
        if right is None:
            return left

        if left.priority > right.priority:
            left.right = self.merge(left.right, right)
            return left
        else:
            right.left = self.merge(left, right.left)
            return right

    def __setitem__(self, key, value):
        """Set the value for the given key in the tree."""
        if self.root is None:
            self.root = TreeNode(key, value)
            self.size += 1
        else:
            self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        """Insert a new key-value pair into the tree or update the value if the key exists."""
        if node is None:
            self.size += 1
            return TreeNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
            if node.left.priority > node.priority:
                node = self._rotate_right(node)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
            if node.right.priority > node.priority:
                node = self._rotate_left(node)
        else:
            node.value = value  # Update the value if the key already exists

        return node

    def __delitem__(self, key):
        """Delete the key-value pair associated with the given key."""
        if self.root is not None:
            self.root = self._delete(self.root, key)
            self.size -= 1
        else:
            raise KeyError(f"Key {key} not found.")

    def _delete(self, node, key):
        """Delete a key from the tree."""
        if node is None:
            raise KeyError(f"Key {key} not found.")

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            return self.merge(node.left, node.right)

        return node

    def __getitem__(self, key):
        """Get the value associated with the given key."""
        return self._find(self.root, key)

    def _find(self, node, key):
        """Find the value associated with the given key in the tree."""
        if node is None:
            raise KeyError(f"Key {key} not found.")
        if key < node.key:
            return self._find(node.left, key)
        elif key > node.key:
            return self._find(node.right, key)
        else:
            return node.value

    def __iter__(self):
        """Return an iterator for the keys in the tree in sorted order."""
        yield from self._inorder(self.root)

    def _inorder(self, node):
        """Perform an in-order traversal of the tree."""
        if node is not None:
            yield from self._inorder(node.left)
            yield node
            yield from self._inorder(node.right)

    def __reversed__(self):
        """Return an iterator for the keys in the tree in reverse sorted order."""
        yield from self._reverse_inorder(self.root)

    def _reverse_inorder(self, node):
        """Perform a reverse in-order traversal of the tree."""
        if node is not None:
            yield from self._reverse_inorder(node.right)
            yield node
            yield from self._reverse_inorder(node.left)

    def _rotate_right(self, node):
        """Perform a right rotation on the node and return the new root."""
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def _rotate_left(self, node):
        """Perform a left rotation on the node and return the new root."""
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    def __len__(self):
        """Return the number of key-value pairs in the tree."""
        return self.size

    def __contains__(self, key):
        """Check if the tree contains the given key."""
        try:
            self[key]
            return True
        except KeyError:
            return False
