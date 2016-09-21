"""Q: Write a method to replace all spaces in a string with '%20' (or
even better, *any* replacement string)."""

from util import test

def urlify(string, rep):
	"""Replace spaces in `string` with `rep`."""
	if string is None or rep is None:
		raise ValueError('Invalid input')

	# Convert to lists, as Python strings are immutable
	string, rep = list(string), list(rep)

	# Append enough runlengh to the end of string
	rep_len = len(rep)
	num_spaces = string.count(' ')
	trail = num_spaces * max((rep_len - 1), 0) # Non-negative trail
	string += ' ' * trail

	# Fill the range [string-length - trail, 0], backwards,
	# so as to not destroy string.
	for i in xrange(len(string) - trail - 1, -1, -1):
		# Space
		if string[i] == ' ':
			trail -= (rep_len - 1) # The space itself accounts for 1
			string[i + trail: i + trail + rep_len] = rep
		# Non-space
		else:
			string[i + trail] = string[i]

	# If rep is empty, string has grown shorter
	if not rep:
		return ''.join(string[-(len(string) - num_spaces):])
	return ''.join(string)

if __name__ == "__main__":
	# Format: (case, result)
	testcases = [(('abc', 'X'), 'abc'),
		(('', 'X'), ''),
		(('', ''), ''),
		(('a b   c', ''), 'abc'),
		(('  ', 'XX'), 'XXXX'),
		(('a b', '%20'), 'a%20b'),
		(('Mr John Smith', '%20'), 'Mr%20John%20Smith'),
		(('ab  ', 'XX'), 'abXXXX'),
		(('a b  ', 'XXXX'), 'aXXXXbXXXXXXXX')]
	test([urlify, ], testcases)
