# A starter kit for the graph/matrix exercise
import collections

def adjlist(adj_list):
	"""
	Read in adj list and store in form of dict mapping node
	name to list of outgoing edges. Preserve the order you find
	for the nodes.
	"""
	adj = collections.OrderedDict() # keep stuff in order read from string

	# fill in

	return adj

def adjmatrix(adj):
	"""
	From an adjacency list, return the adjacency matrix with entries in {0,1}.
	The order of nodes in adj is assumed to be same as they were read in.
	"""
	n = len(adj)
	A = [[0] * n for i in range(n)]

	# fill in

	return A

def nodes(adj, start_node):
	"""
	Walk every node in graph described by adj list starting at start_node
	using a breadth-first search.  Return a list of all nodes found (in
	any order). Include the start_node.
	"""
	nodes = []
	visited = set()
	work = set()

	# fill in

	return nodes

def gendot(adj):
	"""
	Return a string representing the graph in Graphviz DOT format
	with all p->q edges. Parameter adj is an adjacency list.
	"""
	dot = "digraph g {\n"
	dot += "  rankdir=LR;\n"

	# fill in

	dot += "}\n"
	return dot
