"""Q: Given two (singly) linked lists, determine if the two lists
intersect. Return the intersecting node. Note that the intersection
is defined based on reference, not value. That is, if the kth node
of the first linked list is the exact same node (by reference) as
the jth node of the second linked list, then they are intersecting.

ASSUMPTION: The linked lists don't overlap, i.e. have more than
one common node."""

from util import test


class Node(object):
	"""A node in a linked list."""
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def __str__(self):
		return str(self.value) + "-" + str(self.next)

	def __repr__(self):
		return str(self)


def intersection(ll1, ll2):
	"""Return the intersection of `ll1` and `ll2`. Return
	None if they don't intersect.

	"""
	if ll1 is None or ll2 is None:
		raise ValueError('linked list(s) cannot be None')

	def _tail(ll):
		"""Return the tail of `ll`."""
		tail = ll
		while tail.next is not None:
			tail = tail.next
		return tail

	# tails are common => intersection
	tail1, tail2 = _tail(ll1), _tail(ll2)
	if tail1 != tail2:
		return None

	# Connect the tail to one of the heads
	tail1.next = ll2

	# Find the looping node, starting from the other head
	# Step 1: Enter the loop
	slow, fast = ll1, ll1.next
	while slow != fast:
		slow = slow.next
		fast = fast.next.next

	# Step 2: Find the length of the loop
	count = 1
	fast = fast.next
	while slow != fast:
		count += 1
		fast = fast.next

	# Step 3: Find the looping node
	slow = fast = ll1
	for i in xrange(count):
		fast = fast.next
	while slow != fast:
		slow, fast = slow.next, fast.next

	# Restore original input
	tail1.next = None
	return slow.value

if __name__ == "__main__":
	common = Node(4, Node(5))
	ll1 = Node(1, Node(2, Node(3, common)))
	ll2 = Node(3, common)
	ll3 = Node(3, Node(4, Node(5)))
	ll4 = Node(1)
	testcases = [((ll1, ll2), 4),
		((ll1, ll3), None),
		((ll4, ll4), 1)]
	test([intersection], testcases)
