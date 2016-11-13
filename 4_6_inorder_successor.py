"""Q: Write an algorithm to find the "next" node (i.e., in-order
successor) of a given node in a binary search tree. You may assume
that each node has a link to the parent."""

from util import test


class Node(object):
	"""A BST node."""
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

		# Set parent pointers
		self.parent = None # Will be set by parent
		if left is not None:
			self.left.parent = self
		if right is not None:
			self.right.parent = self


def inorder_successor(root, value):
	"""Return the successor of `value` in the in-order
	traversal of the tree rooted at `root`.

	"""
	if root is None or value is None:
		raise ValueError('Tree and value cannot be None')

	def _find(node, value):
		"""Find the node with `value`."""
		if node.value == value:
			return node

		if value < node.value:
			return _find(node.left, value)

		return _find(node.right, value)

	# Find the node of interest
	node = _find(root, value)
	successor = None

	# Case 1: right sub-tree exists
	if node.right is not None:
		successor = node.right
		# Find the left-most element
		while successor.left is not None:
			successor = successor.left

	# Case 2: case 1 is invalid, parent exists and
	# node is on parent's left.
	if successor is None and node.parent is not None \
			and node.parent.left == node:
		successor = node.parent

	# Case 3: cases 1 and 2 have failed. No special
	# operation needed - result is None.
	return successor.value if successor is not None \
		else None

if __name__ == "__main__":
	tree1 = Node(1, Node(0), Node(3, Node(2)))
	tree2 = Node(1, Node(0))
	testcases = [((tree1, 1), 2),
		((tree1, 2), 3),
		((tree1, 3), None),
		((tree2, 1), None)]
	test([inorder_successor, ], testcases)
