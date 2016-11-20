"""Q: T1 and T2 are two very large binary trees, with T1 much bigger than
T2. Create an algorithm to determine if T2 is a subtree of T1."""

from util import test


class Node(object):
	"""A node in a binary tree."""
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.value) + " " \
			+ ("" if self.left is None else str(self.left)) \
			+ ("" if self.right is None else str(self.right))

	def __repr__(self):
		return str(self)


def _identical(root1, root2):
	"""Return True if trees rooted at root1 and root2 are
	identical.

	"""
	# If one of them is None, the other has to be too
	if None in (root1, root2):
		return root1 == root2

	# Step 1: ensure the two values match
	# Step 2: ensure the left subtrees match
	# Step 3: ensure the right subtrees match
	return root1.value == root2.value \
		and _identical(root1.left, root2.left) \
		and _identical(root1.right, root2.right)

def is_subtree(larger, smaller):
	"""Return True if `smaller` is a subtree of `larger`."""
	if None in (larger, smaller):
		raise ValueError('Trees cannot be None')

	# Compare every node with smaller's root, and if
	# matched, check if the subtrees match.
	nodes = [larger]
	while nodes:
		node = nodes.pop(0)
		if node is None:
			continue

		if node.value == smaller.value \
				and _identical(node, smaller):
			return True

		# Add children to the queue
		nodes.extend([node.left, node.right])

	return False

if __name__ == "__main__":
	tree0 = Node(0)
	tree1 = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4)))
	tree2 = Node(1, Node(0), Node(2))
	tree3 = Node(5, Node(4))
	tree4 = Node(4, None, Node(5))
	testcases = [((tree0, tree0), True),
		((tree1, tree0), True),
		((tree1, tree2), True),
		((tree1, tree3), True),
		((tree1, tree4), False),
		((tree2, tree1), False),
		((tree1, Node(3)), False),
		((Node(3), tree1), False),
		((tree1, None), 'Trees cannot be None')]

	test([is_subtree], testcases)
