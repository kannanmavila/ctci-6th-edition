"""Q: Write a program to sort a stack such that the smallest items are on
the top. You can use an additional temporary stack, but you may not
copy the elements into any other data structure (such as an array).
The stack supports the following operations: push, pop, peek and
is_empty."""

from util import test


class Stack(object):
	"""A minimalist stack implementation."""
	def __init__(self, values=[]):
		self.store = values

	def push(self, value):
		self.store.append(value)

	def pop(self):
		return self.store.pop()

	def peek(self):
		return self.store[len(self.store) - 1]

	def is_empty(self):
		return not self.store

	def __str__(self):
		return str(self.store)

	def __repr__(self):
		return str(self)

	def __eq__(self, other):
		return self.store == other.store

	def __ne__(self, other):
		return not self == other


def sort_stack1(stack):
	"""Method 1: Use an auxillary stack

	Time: O(N^2), Space: O(N)

	"""
	if stack is None:
		raise ValueError('Stack cannot be None')

	aux = Stack()
	while not stack.is_empty():
		# As long as elements are in correct order,
		# transfer them to aux.
		if aux.is_empty() or stack.peek() >= aux.peek():
			aux.push(stack.pop())
		# Store the "misplaced" element, transfer larger
		# elements in aux to stack, and then push the
		# misplaced element to stack.
		else:
			temp = stack.pop()
			while not aux.is_empty() and aux.peek() > temp:
				stack.push(aux.pop())
			stack.push(temp)

	# Transfer back (in reverse order)
	while not aux.is_empty():
		stack.push(aux.pop())
	return stack

def sort_stack2(stack):
	"""Method 2: Using recursion and no auxillary stack

	Time: O(N^2), Space: O(N) (internal recursion stack)

	"""
	if stack is None:
		raise ValueError('Stack cannot be None')

	if stack.is_empty():
		return stack

	# Utility to insert a value in the right position
	def _insert(value):
		if stack.is_empty() or stack.peek() > value:
			stack.push(value)
		else:
			temp = stack.pop()
			_insert(value)
			stack.push(temp)

	# Recursively pop, sort and _insert
	temp = stack.pop()
	sort_stack2(stack)
	_insert(temp)
	return stack

if __name__ == "__main__":
	s1 = Stack([4, 1, 6, 2, 3, 8])
	s1_ = Stack([8, 6, 4, 3, 2, 1])
	s2 = Stack([1])
	s2_ = Stack([1])
	s3 = None
	s3_ = 'Stack cannot be None'
	s4 = Stack([1, 2, 3])
	s4_ = Stack([3, 2, 1])
	s5 = Stack([3, 2, 1])
	s5_ = Stack([3, 2, 1])
	s6 = Stack([1, 2, 1])
	s6_ = Stack([2, 1, 1])
	testcases = [((s1, ), s1_),
		((s2, ), s2_),
		((s3, ), s3_),
		((s4, ), s4_),
		((s5, ), s5_),
		((s6, ), s6_)]
	test([sort_stack1, sort_stack2], testcases)
