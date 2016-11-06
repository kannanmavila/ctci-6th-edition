"""Q: Given sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height."""

from util import test


class Node(object):
	"""A node in a tree."""
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __str__(self):
		return (str(self.left) if self.left else "") \
		+ " " + str(self.value) \
		+ (str(self.right) if self.right else "")

	def __repr__(self):
		return str(self)

	def __eq__(self, other):
		if other is None:
			return False
		return self.left == other.left and \
			self.value == other.value and \
			self.right == other.right

	def __ne__(self, other):
		return not self == other


def complete_binary_tree(array):
	"""Return a complete binary tree created out of `array`.

	Parameters:
		array - an increasingly sorted list of numbers

	"""
	# if array is empty or None
	if not array: return None

	# Make the middle element the root and
	# recurse to left and right halves.
	mid = len(array) / 2
	return Node(array[mid],
		complete_binary_tree(array[0:mid]),
		complete_binary_tree(array[mid+1:len(array)]))

if __name__ == "__main__":
	array1 = [1, 2, 3, 4, 5, 6, 7]
	array1_result = Node(4, Node(2, Node(1), Node(3)),
			Node(6, Node(5), Node(7)))
	array2 = [1]
	array2_result = Node(1)
	array3 = [1, 2]
	array3_result = Node(2, Node(1))
	array4 = [1, 2, 3, 4]
	array4_result = Node(3, Node(2, Node(1)), Node(4))

	testcases = [((array1, ), array1_result),
		((array2, ), array2_result),
		((array3, ), array3_result),
		((None, ), None),
		((array4, ), array4_result)]
	test([complete_binary_tree], testcases)
