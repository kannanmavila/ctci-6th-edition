"""Utilities for assisting interview coding practice."""

class TestFailure(Exception):
	"""Failure denoted by a result not matching the
	expected output.

	"""
	pass

def test(function, testcases):
	"""Test `function` using `testcases`, and compare the output
	with expected results.

	Arguments:
		function - the function to be tested
		testcases - a list of tuples, each containing:
			a. a tuple containing arguments to `function`
			b. the expected output for the corresponding input

	"""
	for case, result in testcases:
		output = function(*case)
		print case, "-->", output
		if output != result:
			raise TestFailure("Expected %s, Observed %s"
				% (result, output))
	print "\nAll tests passed!"
