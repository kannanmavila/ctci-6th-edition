"""Q: Design a stack which, in addition to `push` and `pop`, has
a function min which returns the minimum element. `push`, `pop`
and `min` must all operate in O(1) time."""

from util import test


class EmptyStack(IndexError):
	pass


class MinStack(object):
	"""A stack that also stores the minimum element.

	All operations - push, pop and min take O(1) time

	"""
	def __init__(self):
		self.store = []
		self.min = None

	def peek(self):
		"""The top element in the stack."""
		if not self.store:
			raise EmptyStack('Stack is empty')
		return self.store[len(self.store) - 1]

	def push(self, value):
		# First value
		if not self.store:
			self.store.append(value)
			self.min = value

		# Store the information about current min
		elif value < self.min:
			self.store.append(value - self.min)
			self.min = value
		else:
			self.store.append(value)

	def pop(self):
		if not self.store:
			raise EmptyStack('Stack is empty')

		# Restore previous min
		if self.peek() < self.min:
			element = self.min
			self.min = self.min - self.store.pop()

		else:
			element = self.store.pop()

		# Clean up residual min, if exists
		if not self.store: self.min = None
		return element

if __name__ == "__main__":
	stack = MinStack()
	#stack.pop() # EmptyStack
	print stack.min # None
	for i in [3, 4, 2, 2, 5, 1]:
		stack.push(i)
	while stack.store:
		print "min:", stack.min, "popping:", stack.pop()
	print stack.min # None
