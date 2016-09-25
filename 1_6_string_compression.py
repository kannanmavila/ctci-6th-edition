"""Q: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowecase letters (a-z)."""

from util import test

def compress(string):
	"""Return a run-length encoding (RLE) of `string`, if compression
	is possible. Else return `string` itself.

	"""
	if string is None:
		raise ValueError('Invalid input')

	# Sweep and count repeating characters
	run_length = 1
	encoded = ''
	for i in xrange(1, len(string)):
		if string[i] == string[i-1]:
			run_length += 1
		else:
			encoded += string[i-1] + str(run_length)
			run_length = 1

	# Include the last character, unless `string` is empty
	if string:
		encoded += string[-1] + str(run_length)

	# Return `encoded` iff there is improvement
	return encoded if len(encoded) < len(string) \
			else string

if __name__ == "__main__":
	testcases = [(('', ), ''),
		(('a', ), 'a'),
		(('aa', ), 'aa'),
		(('aaa', ), 'a3'),
		(('ababab', ), 'ababab'),
		(('aabcccccaaa', ), 'a2b1c5a3'),
		(('abb', ), 'abb'),
		(('abbb', ), 'abbb'),
		(('abbbb', ), 'a1b4')]
	test([compress, ], testcases)
