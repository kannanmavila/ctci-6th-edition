"""Q: You have two numbers represented by a linked list, where each
node contains a single digit. The digits are stored in reverse
order, such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as
a linked list.

EXAMPLE
Input: 7-1-6 + 5-9-2 (i.e. 617 + 295)
Output: 2-1-9 (i.e. 912)"""

from util import test

class Node(object):
	"""A node in a linked list."""
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


def add(ll1, ll2):
	"""Return a linked list that represents the sum of
	`ll1` and `ll2`. All numbers are represented in reverse,
	i.e. 1's digit is at the head.

	"""
	if ll1 is None or ll2 is None:
		raise ValueError('linked lists cannot be None')

	def _digit(ll):
		"""Fetch the digit, if any, in `ll`."""
		try:
			return ll.value
		except AttributeError:
			return 0

	def _advance(ll):
		"""Return the next node, if any, in `ll`."""
		try:
			return ll.next
		except AttributeError:
			return None

	head = None
	digit_sum = 0
	while ll1 is not None or ll2 is not None:
		digit_sum += _digit(ll1) + _digit(ll2)
		digit = Node(digit_sum % 10)
		if head is None:
			head = tail = digit
		else:
			tail.next = digit
			tail = tail.next
		digit_sum /= 10 # Carry
		ll1, ll2 = _advance(ll1), _advance(ll2)

	# Trailing carry (result longer than both numbers)
	if digit_sum > 0:
		tail.next = Node(digit_sum)

	return head

if __name__ == "__main__":
	n1 = Node(7, Node(1, Node(6)))
	n2 = Node(5, Node(9, Node(2)))
	n1_n2 = Node(2, Node(1, Node(9)))
	n3 = Node(0)
	n4 = Node(0)
	n5 = Node(9)
	n6 = Node(9)
	n5_n6 = Node(8, Node(1))
	n3_n4 = Node(0)
	testcases = [((n1, n2), n1_n2),
		((n3, n4), n3_n4),
		((n5, n6), n5_n6)]
	test([add, ], testcases)
