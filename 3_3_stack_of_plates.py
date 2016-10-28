"""Q: Imagine a (literal) stack of plates. If the stack gets too high,
it might topple. Therefore, in real life, we would likely start a
new stack when the previous stack exceeds some threshold. Implement a
data structure `SetOfStacks` that mimics this. `SetOfStacks` should
be composed of several stacks and should create a new stack once the
previous one exceeds capacity. `push()` and `pop()` should behave
identically to a regular stack.

FOLLOW UP: Implement a function `pop_at(index)` which performs
a pop operation on a specific sub-stack."""


class EmptyStack(IndexError):
	pass


class SetOfStacks(object):
	"""A stack that creates a new sub-task every time
	the size of the current sub-stack exceeds `limit`

	"""
	def __init__(self, limit=float('inf')):
		if limit < 1:
			raise ValueError('Limit must be greater than 0')
		self.stacks = []
		self.limit = limit

	@property
	def current(self):
		"""Current sub-stack in operation."""
		return self.stacks[len(self.stacks) - 1]

	def push(self, value):
		# Fresh start
		if not self.stacks: self.stacks.append([])

		# Size exceeded => created new sub-stack
		if len(self.current) == self.limit:
			self.stacks.append([])

		self.current.append(value)

	def pop(self):
		if not self.stacks:
			raise EmptyStack('Stack is empty')

		# Current sub-stack empty => move to previous
		if not self.current:
			self.stacks.pop()
			return self.pop()

		return self.current.pop()

	def pop_at(self, index):
		"""Pop from the sub-stack at `index`.

		Attributes:
			index - zero-based sub-stack index

		Raises:
			IndexError - when `index` is invalid

		"""
		if not self.stacks:
			raise EmptyStack('Stack is empty')

		if not self.stacks[index]:
			raise EmptyStack('Sub-stack is empty')

		return self.stacks[index].pop()

	def __str__(self):
		return str(self.stacks)

if __name__ == "__main__":
	print "--1--"
	stack = SetOfStacks(3)
	#stack.pop() # EmptyStack
	for i in [1, 2, 3, 4, 5, 6, 7]:
		stack.push(i)
	print stack
	print stack.pop_at(1) # 6
	print stack.pop_at(1) # 5
	print stack.pop_at(1) # 4
	#print stack.pop_at(3) # IndexError
	for i in xrange(4):
		print stack.pop()
		print stack
	#print stack.pop_at(0) # EmptyStack

	print "--2--"
	stack = SetOfStacks(1)
	for i in [1, 2, 3]:
		stack.push(i)
	print stack
	for i in xrange(3):
		print stack.pop()
		print stack

	print "--3--"
	stack = SetOfStacks(0)
	for i in [1, 2]:
		stack.push(i)
	print stack
