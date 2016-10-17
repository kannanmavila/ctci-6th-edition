"""Q: Implement an algorithm to find the kth to last element of a
singly linked list."""

from util import test

class Node(object):
	"""A linkedlist node."""
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def __str__(self):
		return str(self.value) + "-" + str(self.next)

	def __repr__(self):
		return str(self)

class InsufficientNodes(ValueError):
	"""Error raised when there are not enough nodes
	in a linked list.

	"""
	def __init__(self):
		self.message = 'Not enough nodes'

def kth_from_last1(linked_list, k):
	"""Return the kth element from the end of `linked_list`.

	Method 1: Hare-and-tortoise pointers.

	"""
	if linked_list is None:
		raise InsufficientNodes()
	if k <= 0:
		raise ValueError('k must be positive')

	# Advance the fast pointer by k nodes
	fast = slow = linked_list
	for i in xrange(k):
		try:
			fast = fast.next
		except AttributeError:
			raise InsufficientNodes()

	# Advance slow and fast pointers together till the fast
	# one hits the end.
	while fast is not None:
		fast = fast.next
		slow = slow.next

	return slow.value

def kth_from_last2(linked_list, k):
	"""Return the kth element from the end of `linked_list`.

	Method 2: Two loops; first count, and then iterate

	"""
	if linked_list is None:
		raise InsufficientNodes()
	if k <= 0:
		raise ValueError('k must be positive')

	# Count the no. of nodes
	current = linked_list
	count = 0
	while current is not None:
		current = current.next
		count += 1

	# Not enough nodes
	if k > count:
		raise InsufficientNodes()

	# Find the (count-k)th node
	current = linked_list
	for i in xrange(count - k):
		current = current.next

	return current.value

if __name__ == "__main__":
	ll1 = Node(1)
	ll2 = Node(1, Node(2))
	ll3 = Node(1, Node(2, Node(3, Node(4))))
	testcases = [((ll1, 0), 'k must be positive'),
		((ll1, 2), 'Not enough nodes'),
		((ll1, 1), 1),
		((ll2, 2), 1),
		((ll3, 3), 2),
		((ll3, 4), 1)]
	test([kth_from_last1, kth_from_last2], testcases)
