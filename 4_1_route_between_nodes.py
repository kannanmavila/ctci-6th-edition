"""Q: Given a directed graph, design an algorithm to find out whether
there is a route between two nodes."""

from util import test


class Graph(object):
	"""A graph."""
	def __init__(self, values=[]):
		self.edges = {}
		for v in values:
			self.edges[v] = []

	def add_edge(self, source, dest):
		self.edges[source].append(dest)

	def has_edge(self, source, dest):
		return dest in self.edges[source]

	def neighbors(self, vertex):
		return self.edges[vertex]


def has_path(graph, source, dest, visited=[]):
	"""Return True if there is a path from `source` to `dest."""
	if None in (graph, source, dest):
		raise ValueError("graph, source and dest can't be None")

	# See if a neighbor of source is connected to dest
	# or dest itself.
	for neighbor in graph.neighbors(source):
		if neighbor == dest:
			return True

		# Search for paths without looping
		if not (neighbor in visited) and \
		has_path(graph, neighbor, dest, visited + [source]):
			return True

	return False

if __name__ == "__main__":
	graph = Graph([0, 1, 2, 3])
	edges = [(0, 1), (1, 0), (2, 1), (2, 2)]
	for e in edges:
		graph.add_edge(*e)

	testcases = [((graph, 0, 0), True),
		((graph, 0, 1), True),
		((graph, 0, 2), False),
		((graph, 0, 3), False),
		((graph, 1, 0), True),
		((graph, 1, 1), True),
		((graph, 1, 2), False),
		((graph, 1, 3), False),
		((graph, 2, 0), True),
		((graph, 2, 1), True),
		((graph, 2, 2), True),
		((graph, 2, 3), False),
		((graph, 3, 0), False),
		((graph, 3, 1), False),
		((graph, 3, 2), False),
		((graph, 3, 3), False),
		((None, 0, 0), "graph, source and dest can't be None"),
		((graph, None, 0), "graph, source and dest can't be None"),
		((graph, 0, None), "graph, source and dest can't be None")]
	test([has_path], testcases)
