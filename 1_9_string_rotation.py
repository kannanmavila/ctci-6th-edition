"""Q: Assume you have a method is_substring which checks if one word
is a substring of another. Given two string, s1 and s2, write code to
check if s2 is a rotation of s1 using only one call to is_substring
(e.g. "waterbottle" is a rotation of "erbottlewat")."""

from util import test

def _is_substring(s1, s2):
	"""Return True if s2 is a substring of s1."""
	return s1.find(s2) != -1

def is_rotation(s1, s2):
	"""Return True if s1 is a rotation of s2. e.g. 'abcd' is a
	rotation of 'dabc'.

	"""
	if s1 is None or s2 is None:
		raise ValueError('Invalid input')

	# Check if:
	# a. their lengths match
	# b. s1 is a substring of s2 appended to s2
	return len(s1) == len(s2) and _is_substring(s2+s2, s1)

if __name__ == "__main__":
	testcases = [(('', ''), True),
		(('a', 'a'), True),
		(('abcd', 'abc'), False),
		(('abcd', 'cdba'), False),
		(('waterbottle', 'erbottlewat'), True),
		(('aaa', 'aaa'), True),
		(('asdf', 'dfas'), True),
		(('asdf', 'abcd'), False)]
	test([is_rotation, ], testcases)
