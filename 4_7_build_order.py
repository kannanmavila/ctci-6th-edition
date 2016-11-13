"""Q: You are given a list of projects and a list of dependencies
(which is a list of pairs of projects, where the first project is
dependent on the second project). All of a project's dependencies must
be built before the project is. Find a build order that will allow
the projects to be built. If there is no valid build order, return an
error.

EXAMPLE
Input:
	projects: a, b, c, d, e, f
	dependencies: (d, a), (b, f), (d, b), (a, f), (c, d)
Output: f, e, a, b, d, c
"""

from util import test


class CircularDependency(ValueError):
	pass


class Graph(object):
	"""A directed graph."""
	def __init__(self, *values):
		self.edges = {}
		for v in values:
			self.edges[v] = set()

	def add_edge(self, source, dest):
		self.edges[source].add(dest)

	def add_edges(self, *edges):
		for source, dest in edges:
			self.add_edge(source, dest)

	def neighbors(self, node):
		return self.edges[node]

	@property
	def nodes(self):
		return self.edges.keys()


def build_order(graph):
	"""Return a viable build order from the dependency graph
	`graph`.

	Raises:
		CircularDependency - if a viable order doesn't exist

	"""
	if graph is None:
		raise ValueError('Dependency graph is None')

	visited = set()
	build_order = []
	def _topological_sort(node):
		"""Add `node` and its beighbors to the build_order
		depending on their dependencies.

		"""
		if node in visited:
			raise CircularDependency('Cannot be built')

		# Already added to the build order
		if node in build_order:
			return

		# Mark as visited, to detect circular dependencies
		visited.add(node)

		# Add all neighbors (dependencies) to the build
		# order first. And then the node itself.
		for n in graph.neighbors(node):
			_topological_sort(n)
		build_order.append(node)

		visited.remove(node)

	# Trigger the topological sorting of the graph
	for n in graph.nodes:
		_topological_sort(n)

	return build_order

if __name__ == "__main__":
	graph1 = Graph(0)
	graph2 = Graph(0, 1, 2, 3)
	graph2.add_edges((0, 1), (1, 2), (1, 3), (3, 2))
	graph3 = Graph(0, 1, 2, 3)
	graph3.add_edges((0, 1), (1, 2), (3, 2), (0, 3))
	graph4 = Graph(0, 1, 2)
	graph4.add_edges((0, 1), (1, 2), (2, 0))
	graph5 = Graph(0, 1, 2, 3)
	graph5.add_edges((0, 1), (2, 1))
	graph6 = Graph(0, 1, 2)
	graph7 = Graph('a', 'b', 'c', 'd', 'e', 'f')
	graph7.add_edges(('d', 'a'), ('b', 'f'), ('d', 'b'),
		('a', 'f'), ('c', 'd'))

	testcases = [((graph1, ), [0]),
		((graph2, ), [2, 3, 1, 0]),
		((graph3, ), [2, 1, 3, 0]),
		((graph4, ), 'Cannot be built'),
		((graph5, ), [1, 0, 2, 3]),
		((graph6, ), [0, 1, 2]),
		((graph7, ), ['f', 'a', 'b', 'd', 'c', 'e'])]
	test([build_order], testcases)
