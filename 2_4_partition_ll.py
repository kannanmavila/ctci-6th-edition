"""Q: Write code to partition a linked list around a value x, such
that all nodes less than x come before all nodes greater than or equal
to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition
element x can appear anywhere in the "right partition"; it does not
need to appear between left and right partitions.

EXAMPLE:
Input: 3-5-8-5-10-2-1 (partition = 5)
Output: 3-1-2-10-5-5-8
"""

from util import test

class Node(object):
	"""A node in a linked list."""
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def __eq__(self, other):
		return self.value == other.value and \
			self.next == other.next

	def __ne__(self, other):
		return not self == other

	def __str__(self):
		return str(self.value) + "-" + str(self.next)

	def __repr__(self):
		return str(self)


def partition(linked_list, partition):
	"""Modify `linked_list` such that all values less
	than `partition` appear before the values greater
	than or equal to it.

	"""
	if linked_list is None:
		raise ValueError('linked list cannot be None')

	# Reconnect nodes to the beginning and end
	# of the linked list, according to the criterion
	head = tail = linked_list
	current = linked_list.next
	while current is not None:
		next = current.next # Preserve next node
		if current.value < partition:
			current.next = head
			head = current
		else:
			tail.next = current
			tail = current
		current = next # Move ahead
	tail.next = None
	return head

if __name__ == "__main__":
	ll1 = Node(3, Node(5, Node(8, Node(5, Node(10, Node(2, Node(1)))))))
	ll1_result = Node(1, Node(2, Node(3, Node(5, Node(8, Node(5,
		Node(10)))))))
	ll2 = Node(1)
	ll2_result = Node(1)
	ll3 = Node(2, Node(1, Node(2)))
	ll3_result = Node(1, Node(2, Node(2)))

	testcases = [((ll1, 5), ll1_result),
		((ll2, 1), ll2_result),
		((ll2, 2), ll2_result),
		((ll3, 2), ll3_result)]
	test([partition, ], testcases)
