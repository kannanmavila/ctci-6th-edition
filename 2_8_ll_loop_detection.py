"""Q: Given a circular linked list, implement an algorithm that returns
the node at the beginning of the loop."""

from util import test


class Node(object):
	"""A node in a linked list."""
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


def loop_node(linked_list):
	"""Return the node at the beginning of the "loop" in
	`linked_list`.

	"""
	if linked_list is None:
		raise ValueError('Linked list cannot be None')

	# Hare and tortoise pointers
	slow = linked_list
	fast = linked_list.next
	while slow != fast:
		try:
			slow = slow.next
			fast = fast.next.next
		# There is no loop
		except AttributeError:
			return None

	# Find the length of the loop
	count = 1
	fast = fast.next
	while fast != slow:
		count += 1
		fast = fast.next

	# Find the looping point using "train" pointers
	slow = fast = linked_list
	for i in xrange(count):
		fast = fast.next
	while slow != fast:
		slow = slow.next
		fast = fast.next
	return slow.value

if __name__ == "__main__":
	n1 = Node(3)
	ll1 = Node(1, Node(2, n1))
	n1.next = ll1

	ll2 = Node(1)
	ll2.next = ll2

	ll3 = Node(1, Node(2))
	ll3.next.next = ll3.next

	ll4 = Node(1, Node(2, Node(3, Node(4))))

	testcases = [((ll1, ), 1),
		((ll2, ), 1),
		((ll3, ), 2),
		((None, ), 'Linked list cannot be None'),
		((ll4, ), None)]
	test([loop_node, ], testcases)
