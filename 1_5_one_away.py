"""Q: There are three types of edits that can be performed on
strings: insert a character, remove a character, or replace a
character. Given two strings, write a function to check if they
are one edit (or zero edits) away."""

from util import test

def is_one_away1(string1, string2):
	"""Return True if string2 can be created by removing, adding
	or replacing a character from string1.

	"""
	if string1 is None or string2 is None:
		raise ValueError('Invalid input')

	# Ensure that length difference is not more than 1
	if abs(len(string1) - len(string2)) > 1:
		return False

	# Iterate over the shorter string
	for i in xrange(min(len(string1), len(string2))):
		if string1[i] == string2[i]:
			continue

		# Case 1: Replacement
		if string1[i+1:] == string2[i+1:]:
			return True

		# Case 2: Removal/addition
		if string1[i+1:] == string2[i:] or \
				string1[i:] == string2[i+1:]:
			return True

		return False

	# Case 3: Identical or
	# Case 2a: Addition at the end of the longer string
	return True

if __name__ == "__main__":
	testcases = [(('', ''), True),
		(('', 'a'), True),
		(('a', 'b'), True),
		(('abccde', 'abcde'), True),
		(('abde', 'abcde'), True),
		(('abcd', 'abed'), True),
		(('abcd', 'abde'), False),
		(('abbcd', 'abccd'), True),
		(('abc', 'cde'), False),
		(('asdf', 'abcd'), False),
		(('abc', 'bca'), False)]
	test([is_one_away1], testcases)
