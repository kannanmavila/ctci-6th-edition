"""Q: Implement a function to check if a binary tree is balanced.
For the purposes of this question, a balanced binary tree is defined
to be a tree such that heights of the two subtrees of any node
never differ by more than one."""

from util import test


class Node(object):
	"""A node in a binary tree."""
	def __init__(self, left=None, right=None):
		self.left = left
		self.right = right


def is_balanced(root):
	"""Return True if no two subtrees of any node under `root`
	has heights differing by more than one.

	"""
	if root is None:
		raise ValueError('Tree cannot be None')

	# Method to recursively calculate the heights of
	# sub-trees, and check balance at the same time
	def _is_balanced(node):
		"""Returns:
			is_balanced - True if subtrees are balanced
			height - max height of subtrees

		"""
		if node is None:
			return True, 0

		left_balanced, left_height = _is_balanced(node.left)
		right_balanced, right_height = _is_balanced(node.right)

		# 1. Make sure that left and right subtrees are
		# individually balanced, and that the subtree
		# rooted at `node` is too.
		this_balanced = left_balanced and right_balanced \
			and abs(left_height - right_height) <= 1
		this_height = 1 + max(left_height, right_height)
		return this_balanced, this_height

	return _is_balanced(root)[0]

if __name__ == "__main__":
	root1 = Node()
	root2 = Node(Node(Node()), Node(None, Node()))
	root3 = Node(Node(Node()))
	root4 = Node(Node(Node(Node())), Node(None, Node(None, Node())))
	root5 = Node(Node(Node(Node()), Node()), Node(None, Node()))
	testcases = [((None, ), 'Tree cannot be None'),
		((root1, ), True),
		((root2, ), True),
		((root3, ), False),
		((root4, ), False),
		((root5, ), True)]
	test([is_balanced], testcases)
