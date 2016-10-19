"""Q: Implement a function to check if a linked list is a palindrome"""

from util import test


class Node(object):
	"""A node in a linked list."""
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
	"""
	def __eq__(self, other):
		return other is not None and \
			self.value == other.value and \
			self.next == other.next

	def __ne__(self, other):
		return not self == other
	"""
	def __str__(self):
		return str(self.value) + "-" + str(self.next)

	def __repr__(self):
		return str(self)


def is_palindrome(linked_list):
	"""Return True if `linked_list` is a palindrome."""
	if linked_list is None:
		raise ValueError('linked list cannot be None')

	def _reverse(head):
		"""Reverse the linked list starting at `head` and
		return the new head.

		"""
		current = head
		next = head.next
		head.next = None
		while next is not None:
			temp = next.next
			next.next = current
			current, next = next, temp
		return current

	# Find the middle node
	middle = end = linked_list
	while end is not None and end.next is not None:
		end = end.next.next
		middle = middle.next

	# Reverse the later half (starting at middle)
	end = _reverse(middle)

	# Compare the two halves:
	# 1. start --> middle
	# 2. middle <-- end
	while True:
		if linked_list.value != end.value:
			return False
		if end == middle:
			break
		linked_list = linked_list.next
		end = end.next # Move "backwards"

	# Restore the input
	_reverse(middle)
	return True

if __name__ == "__main__":
	ll1 = Node(1, Node(2, Node(3, Node(2, Node(1)))))
	ll2 = Node(1)
	ll3 = Node(1, Node(2, Node(2, Node(1))))
	ll4 = Node(1, Node(1))
	ll5 = Node(1, Node(2, Node(3, Node(4))))
	ll6 = Node(1, Node(2))
	ll7 = Node(1, Node(2, Node(3)))

	testcases = [((ll1, ), True),
		((ll2, ), True),
		((ll3, ), True),
		((ll4, ), True),
		((ll5, ), False),
		((ll6, ), False),
		((ll7, ), False)]
	test([is_palindrome, ], testcases)
