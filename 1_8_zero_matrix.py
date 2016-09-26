"""Q: Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0."""

from util import test

def zero(matrix):
	"""Return a copy of the matrix where every row and
	column with a zero, is completely zeroed out.

	"""
	if matrix is None or len(matrix) == 0:
		raise ValueError('Invalid input')

	m = len(matrix)
	n = len(matrix[0])

	# Mark rows and columns to be zeroed. They cannot
	# be zeroed in one go, because that will lead to
	# loss of information about which cells were originally
	# zero, and which ones were zeroed out.
	# This can be done in O(1) space using the first row
	# and first column to store the to-be-zeroed flag. After
	# all, we never *go back* to those values, so this will
	# not cause the "confusion" explained above.
	for i in xrange(m):
		# Matrix must be rectangular
		if len(matrix[i]) != n:
			raise ValueError('Matrix must be rectangular.')
		for j in xrange(n):
			if matrix[i][j] == 0:
				matrix[i][0] = matrix[0][j] = 0

	# Zero out the values, starting from bottom-right
	for i in xrange(m-1, -1, -1):
		for j in xrange(n-1, -1, -1):
			if 0 in (matrix[i][0], matrix[0][j]):
				if (i, j) == (2, 3): print "$$$", matrix[i][0], matrix[0][j]
				matrix[i][j] = 0

	return matrix

if __name__ == "__main__":
	matrix1 = [
		[1, 0, 5, 9],
		[0, 1, 0, 9],
		[6, 3, 4, 5]]
	matrix1_zeroed = [
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 5]]
	testcases = [(([[]], ), [[]]),
		(([[0]], ), [[0]]),
		((matrix1, ), matrix1_zeroed)]
	test([zero, ], testcases)
