"""Q: You are given a binary search tree in which each node contains
an integer value (which might be positive or negative). Design an
algorithm to count the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, but
it must go downwards (traveling only from parent nodes to
child nodes)."""

from util import test


class Node(object):
	"""A node in a binary tree."""
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def sum_paths(root, target):
	"""Return the no. of paths in the tree rooted at `root`,
	that sum up to `target`. Paths do not have to start at
	the root node or end at a leaf node, but have to be
	a contiguous downward path.

	Time: O(N), Space: O(log N)

	"""
	if root is None or target is None:
		raise ValueError('Tree or target cannot be None')

	# A dictionary that maps a value against no. of paths
	# from root that sum up to that value.
	paths = {0: 1} # Empty path

	def _paths_ending_here(node, sum_so_far):
		if node is None:
			return 0

		# Update the entry for this value
		sum_so_far += node.value
		paths[sum_so_far] = paths.setdefault(sum_so_far, 0) + 1

		# As many valid paths can end here as there are
		# paths from root that sum up to the difference
		# between sum_so_far and target.
		valid_paths = _paths_ending_here(node.left, sum_so_far) \
			+ _paths_ending_here(node.right, sum_so_far)

		# NB: If we now add paths ending at this node,
		# it will result in a bug when target is zero.
		# In that case, we will "subtract" the path
		# ending here from itself, resulting in an empty
		# path being counter. As a result, the output will
		# be off by no. of nodes in the tree (as this will
		# happen at every node).

		# Update the entry for this value (only the children
		# can use the path through this node).
		paths[sum_so_far] -= 1

		return valid_paths \
			+ paths.setdefault(sum_so_far - target, 0)

	return _paths_ending_here(root, 0)

if __name__ == "__main__":
	tree0 = Node(-1, Node(-2, Node(-3, Node(-3))))
	tree1 = Node(3, Node(2, Node(1, Node(-3)), Node(-2)),
			Node(-2, Node(2), Node(-3)))
	testcases = [((tree0, 0), 0),
		((tree0, -1), 1),
		((tree0, -2), 1),
		((tree0, -3), 3),
		((tree0, -6), 2),
		((tree1, 0), 3),
		((tree1, 3), 5),
		((tree1, -2), 4)]

	test([sum_paths], testcases)
