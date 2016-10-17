"""Utilities for assisting interview coding practice."""

class TestFailure(Exception):
	"""Failure denoted by a result not matching the
	expected output.

	"""
	pass


def run_function(function, input):
	"""Run `function` with the specified input, and
	stringify errors if any.

	"""
	try:
		output = function(*input)
	except Exception as e:
		return e.message
	return output

def test(functions, testcases):
	"""Test every function in `functions` using `testcases`,
	and compare the output with expected results.

	Arguments:
		functions - a list of alternate functions that must
			produce identical results
		testcases - a list of tuples, each containing:
			a. a tuple containing arguments to the functions
			b. the expected result for the corresponding input

	TODO: Deep copy input before passing to functions, so that
	in-place modifications do not mutilate the original input.

	"""
	for input, result in testcases:
		outputs = [run_function(f, input) for f in functions]

		# Ensure that functions produce identical outputs.
		# Earlier version created a set and ensured that
		# the length is 1. But this failed for unhashable
		# types. Hence this naive implementation.
		for i in xrange(1, len(outputs)):
			if outputs[i] != outputs[i-1]:
				raise TestFailure("Functions disagree"
						" about %s. Outputs:\n%s"
						% (input, outputs))

		# Display input and output
		print input, "-->", outputs[0] # Print any output

		# Test the output against the expected result
		if outputs[0] != result:
			raise TestFailure("Expected %s" % result)
	print "\nSUCCESS!"
