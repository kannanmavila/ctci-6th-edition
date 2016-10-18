"""Q: Write code to remove duplicates from an unsorted linked list.

Follow up: How would you solve this problem if a temporary buffer
is not allowed?"""

from util import test
from copy import deepcopy

class Node(object):
	"""A linked-list node."""
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def __eq__(self, other):
		return other is not None and \
			self.value == other.value and \
			self.next == other.next

	def __ne__(self, other):
		return not self == other

	def __str__(self):
		return str(self.value) + "-" + str(self.next)

	def __repr__(self):
		return str(self)

def dedup1(linked_list):
	"""Return `linked_list` with duplicates removed.

	Method 1: Mark (hash) and sweep.
	Time: O(N), Space: O(N)

	"""
	if linked_list is None:
		raise ValueError('Invalid input')

	# Mark and sweep
	current = linked_list
	seen = set([current.value])
	while current.next is not None:
		if current.next.value in seen:
			current.next = current.next.next
		else:
			current = current.next # Move forward

	return linked_list

def dedup2(linked_list):
	"""Return `linked_list` with duplicates removed.

	Method 2: "Loop" twice
	Time: O(N^2), Space: O(1)

	NB: The only difference is the way `seen` is implemented.

	"""
	if linked_list is None:
		raise ValueError('Invalid input')

	def _seen(node):
		"""Return True if `node` has already been seen *earlier*
		in the linked list.

		"""
		check = linked_list
		while check != node:
			if check.value == node.value:
				return True
			check = check.next
		return False

	# Iterate through the list
	current = linked_list
	while current.next is not None:
		if _seen(current.next):
			current.next = current.next.next
		else:
			current = current.next # Move forward

	return linked_list

if __name__ == "__main__":
	ll1 = Node(1, Node(2, Node(3)))
	ll1_result = deepcopy(ll1)
	ll2 = Node(1)
	ll2_result = deepcopy(ll2)
	ll3 = Node(1, Node(1, Node(1)))
	ll3_result = Node(1)
	ll4 = Node(1, Node(2, Node(1)))
	ll4_result = Node(1, Node(2))

	testcases = [((ll1, ), ll1_result),
		((ll2, ), ll2_result),
		((ll3, ), ll3_result),
		((ll4, ), ll4_result)]
	test([dedup1, dedup2], testcases)
