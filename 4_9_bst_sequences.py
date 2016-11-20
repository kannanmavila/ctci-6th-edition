"""Q: A binary search tree was created by traversing through an array
from left to right and inserting each element. Given a binary search
tree with distinct elements, print all possible arrays that could have
led to this tree.

EXAMPLE

Input:
   2
  / \
 1   3

Output: {2, 1, 3}, {2, 3, 1}

"""

from util import test


class Node(object):
	"""A node in a binary tree."""
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def _topological_combine(a, b, prefix=[]):
	"""Return all the combinations of the lists a and b,
	such that every element appears after its predecessors
	in its original list (a or b).

	"""
	if not a: return [prefix + b]
	if not b: return [prefix + a]

	# Step 1: add a's first element to prefix and recurse
	# Step 2: add b's first element to prefix and recurse
	combinations = []
	combinations.extend(_topological_combine(a[1:], b, prefix + [a[0]]))
	combinations.extend(_topological_combine(a, b[1:], prefix + [b[0]]))

	return combinations

def possible_array_sequences(root):
	"""Return all possible array sequences from which the BST
	rooted `root` could've been created.

	"""
	# Recursive utility method
	def _pas(node):
		if node is None:
			return []

		# Get all possible sequences from left and right
		# subtrees.
		left_sequences = _pas(node.left)
		right_sequences = _pas(node.right)

		# Combine them topologically (such that no child comes
		# before its parent).
		combinations = []
		for l in left_sequences:
			for r in right_sequences:
				combinations.extend(_topological_combine(l, r))

		# If one of the sub-trees is empty, ignore it
		# (this is a short-hand trick).
		if not combinations:
			combinations = left_sequences + right_sequences

		# This node is a leaf node (i.e. both left and right
		# sub-trees are empty).
		if not combinations:
			return [[node.value]]

		# Prepend this node's value to every combination
		return [[node.value] + c for c in combinations]

	return _pas(root)

if __name__ == "__main__":
	tree0 = Node(2, Node(1), Node(3))
	tree0_result = [[2, 1, 3], [2, 3, 1]]
	tree1 = Node(0)
	tree2 = Node(3, Node(1, Node(0), Node(2)), Node(4))
	tree2_result = [[3, 1, 0, 2, 4],
		[3, 1, 0, 4, 2],
		[3, 1, 4, 0, 2],
		[3, 4, 1, 0, 2],
		[3, 1, 2, 0, 4],
		[3, 1, 2, 4, 0],
		[3, 1, 4, 2, 0],
		[3, 4, 1, 2, 0]]
	testcases = [((tree0, ), tree0_result),
		((tree1, ), [[0]]),
		((tree2, ), tree2_result)]

	test([possible_array_sequences], testcases)
