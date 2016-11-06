"""Q: Given a binary tree, design an algorithm which creates a linked
list of all the nodes at each depth (e.g. if you have a tree with
depth D, you'll have D linked lists)."""

from util import test


class TreeNode(object):
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


class ListNode(object):
	"""A node in a linked-list."""
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def __str__(self):
		return str(self.value) + "->" \
			+ (str(self.next) if self.next else "")

	def __repr__(self):
		return str(self)

	def __eq__(self, other):
		if other is None:
			return False
		return self.value == other.value \
			and self.next == other.next

	def __ne__(self, other):
		return not self == other


def level_lists(tree):
	"""Return a list containing linked-lists formed out
	of elements at each level. e.g.
		1
	       / \
	      2   3 returns [1->None, 2->3->None]

	"""
	if tree is None:
		raise ValueError('Tree cannot be None')

	# Perform BFS, and create linked-lists for each level
	lists = []
	queue = [tree.left, tree.right]
	head = ListNode(tree.value)
	count = 1
	while queue:
		tree_node = queue.pop(0)
		count -= 1
		if tree_node is None:
			continue
		list_node = ListNode(tree_node.value)

		# Add old level to the list and start new level
		if count == 0:
			print "count is zero at:", list_node.value
			lists.append(head)
			head = tail = list_node
			count = len(queue) + 1 # +1 for the current node

		# Add to current level
		else:
			tail.next = list_node
			tail = list_node

		# Add non-None children to the queue
		if tree_node.left is not None:
			queue.append(tree_node.left)
		if tree_node.right is not None:
			queue.append(tree_node.right)

	lists.append(head)
	return lists

if __name__ == "__main__":
	tree1 = TreeNode(1, TreeNode(2, TreeNode(4),
				TreeNode(5, TreeNode(7), TreeNode(8))),
			TreeNode(3, TreeNode(6)))
	tree1_result = [ListNode(1),
		ListNode(2, ListNode(3)),
		ListNode(4, ListNode(5, ListNode(6))),
		ListNode(7, ListNode(8))]
	tree2 = TreeNode(1)
	tree2_result = [ListNode(1), ]
	tree3 = TreeNode(1, TreeNode(2, TreeNode(3)))
	tree3_result = [ListNode(1), ListNode(2), ListNode(3)]

	testcases = [((tree1, ), tree1_result),
		((tree2, ), tree2_result),
		((tree3, ), tree3_result)]
	test([level_lists], testcases)
