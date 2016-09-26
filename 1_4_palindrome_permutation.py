"""Q: Given a string, write a function to check if it is a
permutation of a palindrome."""

from util import test

def is_palindrome_permutation1(string):
	"""Return True if `string` is a permutation of a palindrome.

	Method 1: Hash and match characters. Ensure unmatching <= 1
	Time: O(N)
	Space: O(N)

	"""
	if string is None:
		raise ValueError('Invalid input')

	# "Pair up" characters
	paired = {}
	for c in string:
		paired.setdefault(c, True)
		paired[c] = not paired[c]

	# Ensure there's not more than one unpaired character
	# 0 => identical halves, 1 => unpaired middle character
	return paired.values().count(False) <= 1

def is_palindrome_permutation2(string):
	"""Return True if `string` is a permutation of a palindrome.

	Method 2: Sort and sweep
	Time: O(NlogN)
	Space: O(1)

	"""
	if string is None:
		raise ValueError('Invalid input')

	# Sort the input (string is immutable, hence convert to list)
	string = ''.join(sorted(string))

	# Sweep for sets of characters and ensure ever set has an even
	# number of elements, with a possible single exception, which
	# may be the middle element in the palindrome
	odds = 0
	current = 1
	for i in xrange(1, len(string)):
		# Still in the current run
		if string[i] == string[i-1]:
			current += 1
		else:
			# Previous character occurred odd# of times
			if current%2 == 1:
				odds += 1
			# Start a new run
			current = 1

	# 1. If no odd groups found, the last "current" is permitted,
	# since it can be the middle element.
	# 2. If there is an odd group already, last "current"
	# cannot be odd too.
	# 3. If there's more than one odd group, it's not a palindrome.
	return odds == 0 or \
		(odds == 1 and current % 2 == 0)

if __name__ == "__main__":
	testcases = [(('', ), True),
		(('a', ), True),
		(('ab', ), False),
		(('aaa', ), True),
		(('abccba', ), True),
		(('abcab', ), True),
		(('aaabbb', ), False),
		(('asdf', ), False),
		(('asdfas', ), False)]
	test([is_palindrome_permutation1, is_palindrome_permutation2],
		testcases)
