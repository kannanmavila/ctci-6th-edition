"""Q: Given two strings, write a method to decide if one is a permutation of the other."""

from util import test

def is_permutation1(string1, string2):
	"""Return True if `string1` is a permutation of `string2`.

	Method 1: Hash the character counts and tally.
	Time: O(N)
	Space: O(N)

	"""
	if string1 is None or string2 is None:
		raise ValueError('Invalid input')

	# Count character occurrences in string1
	count = {}
	for c in string1:
		count[c] = count.get(c, 0) + 1

	# Cancel out occurrences in string2
	for c in string2:
		try:
			count[c] -= 1
		# c doesn't exist in string1
		except KeyError:
			return False

	# Ensure all characters "cancelled out"
	for c in count:
		if count[c] != 0:
			return False
	return True

def is_permutation2(string1, string2):
	"""Return True if `string1` is a permutation of `string2`.

	Method 2: Sort and compare.
	Time: O(NlogN)
	Space: O(1)

	"""
	return sorted(string1) == sorted(string2)

if __name__ == "__main__":
	testcases = [(('', ''), True),
		(('aab', 'ab'), False),
		(('123', '231'), True),
		(('a', 'a'), True),
		(('asddfda', 'adafdsd'), True)]
	test([is_permutation1, is_permutation2], testcases)
