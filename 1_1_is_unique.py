"""Q: Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?"""

from util import test

def is_unique1(string):
	"""Return True if `string` has no duplicate character.

	Method 1: Hashtable.
	Time: O(N), Space: O(N)

	"""
	if string is None:
		raise ValueError('Not a valid string')

	seen = set()
	for c in string:
		if c in seen:
			return False
		seen.add(c)
	return True

def is_unique2(string):
	"""Return True if `string` has no duplicate character.

	Method 2: Sort and search.
	Time: O(NlogN), Space: O(1)

	"""
	if string is None:
		raise ValueError('Not a valid string')

	string = sorted(string)

	# Check if adjacent characters are the same
	for i in xrange(0, len(string)-1):
		if string[i] == string[i+1]:
			return False
	return True

if __name__ == "__main__":
	testcases = [(('aa', ), False),
		(('abc', ), True),
		(('', ), True),
		(('a', ), True)]
	test([is_unique1, is_unique2], testcases)
