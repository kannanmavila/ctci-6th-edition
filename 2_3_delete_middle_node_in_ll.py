"""Q: Implement an algorithm to delete a node in the middle
(i.e., any node but the first and last node, not necessarily the
exact middle) of a singly linked list, given only access to that node"""

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

def delete_node(node):
	"""Delete `node` from its linked list. `node` is neither
	the first node, nor the last.

	"""
	if node is None:
		raise ValueError('node cannot be None')

	while node.next is not None:
		node.value = node.next.value
		if node.next.next is None:
			node.next = None
			break # Else next loop will raise AttributeError
		node = node.next

if __name__ == "__main__":
	ll1 = Node(1, Node(2, Node(3)))
	ll2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
	testcases = [((ll1.next, ), None),
		((ll2.next, ), None),
		((ll2.next.next, ), None)]
	test([delete_node, ], testcases)
	print ll1, ll2
