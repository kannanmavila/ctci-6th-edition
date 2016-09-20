"""Q: Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?"""

from util import test

def is_unique(string):
	"""Return True if `string` has no duplicate character."""
	if string is None:
		raise ValueError('Not a valid string')

	result = _is_unique1(string)
	assert result == _is_unique2(string)
	return result

def _is_unique1(string):
	"""Method 1: Hashtable.
	Time: O(N), Space: O(N)

	"""
	seen = set()
	for c in string:
		if c in seen:
			return False
		seen.add(c)
	return True

def _is_unique2(string):
	"""Method 2: Sort and search.
	Time: O(NlogN), Space: O(1)

	"""
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
	test(is_unique, testcases)
