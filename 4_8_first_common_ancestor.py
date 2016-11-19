"""Q: Design an algorithm and write code to find the first common
ancestor of two nodes in a binary tree. Avoid storing additional
nodes in a data structure. NOTE: This is not necessarily a binary
search tree."""

from util import test


class Node(object):
	"""A node in a binary tree."""
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def first_common_ancestor(root, a, b):
	"""Return the first (lowest) common ancestor of `a` and `b`,
	in the binary tree rooted at `root`.

	Returns:
		None - if a and/or b do/does not exist

	"""
	# Util function for recursion
	def _fca(node):
		if node is None:
			return None, False, False

		# Get stats about the sub-trees
		left_ancestor, left_has_a, left_has_b = _fca(node.left)
		right_ancestor, right_has_a, right_has_b = _fca(node.right)
		ancestor = left_ancestor or right_ancestor
		has_a = left_has_a or right_has_a
		has_b = left_has_b or right_has_b

		# Already found an ancestor in a subtree
		if ancestor is not None:
			return ancestor, True, True

		# This node is the ancestor
		if has_a and has_b:
			return node, True, True

		return (ancestor,
			has_a or node.value == a,
			has_b or node.value == b)

	result = _fca(root)[0]
	return result.value if result is not None else None

if __name__ == "__main__":
	tree0 = Node(0)
	tree1 = Node(0, Node(1, Node(3), Node(4)), Node(2))
	tree2 = Node(0, Node(0), Node(0))
	testcases = [((tree0, 0, 0), None),
		((tree1, 1, 2), 0),
		((tree1, 3, 1), 0),
		((tree1, 3, 4), 1),
		((tree1, 1, 0), None),
		((tree1, 5, 6), None),
		((tree1, 4, 5), None),
		((tree2, 0, 0), 0)]
	test([first_common_ancestor], testcases)
