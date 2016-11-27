"""Q: You are implementing a binary tree class from scratch which,
in addition to insert, find and delete, has a method getRandomNode()
which returns a random node from the tree. All nodes should be equally
likely to be chosen. Design and implement an algorithm for getRandomNode,
and explain how you would implement the rest of the methods."""

from random import randrange


class Node(object):
	"""A node in a RandomTree."""
	def __init__(self, value, size=1):
		self.value = value
		self.size = size
		self.left = None
		self.right = None

	def __str__(self):
		left = "" if self.left is None else str(self.left)
		right = "" if self.right is None else str(self.right)
		return left \
			+ " (" + str(self.value) \
			+ ", " + str(self.size) + ")" \
			+ right

	def __repr__(self):
		return str(self)

class RandomTree(object):
	"""A tree capable of returning a node at random."""
	def __init__(self):
		self.root = None

	def __str__(self):
		return str(self.root)

	def __repr__(self):
		return str(self)

	def insert(self, *values):
		for v in values:
			self._insert(v)

	def _insert(self, value):
		# Empty tree
		if self.root is None:
			self.root = Node(value)
			return

		node = self.root
		while True:
			# Increase the subtree size
			node.size += 1

			# Branch left
			if value < node.value:
				if node.left is None:
					node.left = Node(value)
					return
				node = node.left

			# Branch right
			else:
				if node.right is None:
					node.right = Node(value)
					return
				node = node.right

	def find(self, value):
		# Empty tree
		if self.root is None:
			raise IndexError('Empty tree')

		node = self.root
		while node is not None:
			if value == node.value:
				return True
			node = node.left if value < node.value \
				else node.right
		return False

	def delete(self, value):
		# Empty tree
		if self.root is None:
			raise IndexError('Empty tree')

		# Value not found
		if not self.find(value):
			raise ValueError('Value not found')

		# Find the node and the parent
		parent, node = None, self.root
		while node.value != value:
			parent = node
			parent.size -= 1
			node = node.left if value < node.value else node.right

		# Substitute the node
		# Case 1: leaf node; no substitution
		if node.left is None and node.right is None:
			# Deleting the only node (root)
			if parent is None:
				self.root = None
			elif parent.left == node:
				parent.left = None
			else:
				parent.right = None
			return

		# Case 2: has right subtree; replace with left-most
		# child of the right subtree.
		if node.right is not None:
			node.size -= 1
			parent, sub = node, node.right
			sub.size -= 1
			while sub.left is not None:
				parent, sub = sub, sub.left
				sub.size -= 1

			# Replace node with sub
			node.value = sub.value # Replace node with sub

			# Delete sub
			if parent.left == sub:
				parent.left = None
			else:
				parent.right = None

		# Case 3: has only left subtree; replace with node.left
		else:
			# Deleting root node
			if parent is None:
				self.root = node.left
			elif parent.left == node:
				parent.left = node.left
			else:
				parent.right = node.left

	def get_random(self):
		"""Return a random node value."""
		node = self.root
		while True:
			lottery = randrange(node.size)
			if lottery == 0:
				return node.value

			if node.left is None or lottery > node.left.size:
				node = node.right
			else:
				node = node.left
