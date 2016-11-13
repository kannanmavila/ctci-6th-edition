"""Q: Implement a function to check if a binary tree is a binary
search tree."""

from util import test

class Node(object):
	"""A binary tree node."""
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def is_bst(node, low=-float('inf'), high=float('inf')):
	"""Return True if the binary tree rooted at `node` is
	a binary search tree.

	"""
	if node is None:
		return True

	# 1. Ensure current node doesn't violate boundaries
	# 2. Ensure left sub-tree doesn't
	# 3. Ensure right sub-tree doesn't
	return (low < node.value < high) \
		and is_bst(node.left, low, node.value) \
		and is_bst(node.right, node.value, high)

if __name__ == "__main__":
	tree1 = Node(1)
	tree2 = Node(1, Node(0), Node(2))
	tree3 = Node(1, Node(0))
	tree4 = Node(2, Node(1, Node(0), Node(3)), Node(4))
	tree5 = Node(1, None, Node(0))
	testcases = [((tree1, ), True),
		((tree2, ), True),
		((tree3, ), True),
		((tree4, ), False),
		((tree5, ), False)]
	test([is_bst, ], testcases)
