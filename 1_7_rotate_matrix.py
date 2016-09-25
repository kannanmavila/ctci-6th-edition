"""Q: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?"""

from util import test

def rotate_90_degrees(matrix, clockwise=True):
	"""Rotate `matrix` by 90 degrees, clockwise or anti-clockwise
	depending on `clockwise`.

	"""
	if matrix is None or clockwise is None:
		raise ValueError('Invalid input')

	n = len(matrix)

	def _swap(x1, y1, x2, y2):
		"""Swap matrix[x1][y1] and matrix[x2][y2] in place."""
		matrix[x1][y1], matrix[x2][y2] = \
				matrix[x2][y2], matrix[x1][y1]

	# Create the transpose of `matrix`, in place
	for i in xrange(n):
		for j in xrange(i):
			_swap(i, j, j, i)

	# Rotate
	for i in xrange(n):
		for j in xrange(n/2):
			# clockwise: flip `matrix` horizontally
			if clockwise:
				_swap(i, j, i, n-j-1)
			# anti-clockwise: flip `matrix` vertically
			else:
				_swap(j, i, n-j-1, i)

	return matrix

if __name__ == "__main__":
	matrix1 = [
		[0, 1, 2],
		[3, 4, 5],
		[6, 7, 8]]
	matrix1_cw = [
		[6, 3, 0],
		[7, 4, 1],
		[8, 5, 2]]
	matrix2 = [
		[0, 1, 2],
		[3, 4, 5],
		[6, 7, 8]]
	matrix2_ccw = [
		[2, 5, 8],
		[1, 4, 7],
		[0, 3, 6]]
	testcases = [(([[]], ), [[]]),
		(([[0]], ), [[0]]),
		((matrix1, ), matrix1_cw),
		((matrix2, False), matrix2_ccw)]

	test([rotate_90_degrees, ], testcases)
