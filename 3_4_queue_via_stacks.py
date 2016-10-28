"""Q: Implement a `MyQueue` class which implements a queue using
two stacks."""


class EmptyQueue(IndexError):
	pass


class MyQueue(object):
	"""A queue using two stacks."""
	def __init__(self):
		self.push_stack = []
		self.pop_stack = []

	def _move(self):
		"""Transfer push_stack to pop_stack, if the latter
		is empty.

		Raises:
			EmptyQueue - If both stacks are empty

		"""
		if not self.pop_stack:
			if not self.push_stack:
				raise EmptyQueue('Queue is empty')
			while self.push_stack:
				self.pop_stack.append(self.push_stack.pop())

	def push(self, value):
		self.push_stack.append(value)

	def pop(self):
		self._move()
		return self.pop_stack.pop()

	def peek(self):
		self._move()
		count = len(self.pop_stack)
		return self.pop_stack[count - 1]

	def __str__(self):
		return str(self.push_stack) + "\n" + str(self.pop_stack)


if __name__ == "__main__":
	queue = MyQueue()
	# print queue.pop() # EmptyQueue
	for i in [1, 3, 4, 6, 2, 3]:
		queue.push(i)
	for i in xrange(6):
		print queue.pop()

	for i in [1, 2, 3, 4, 5]:
		queue.push(i)
	for i in xrange(2):
		queue.pop()
	print queue
	queue.pop()
	print queue
	queue.push(6)
	print queue
	for i in xrange(3):
		print queue.pop()
		print queue
