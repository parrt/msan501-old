from graph import *

# support code

def chktargets(start, expecting):
	if adj[start] != expecting:
		print "error for", start, ": expecting", expecting, "found", adj[start]

def checknodes(start, expecting):
	result = nodes(adj, start)
	if set(result) != set(expecting):
		print "error starting at", start, ": expecting", expecting, "found", result

data = """
parrt: tombu, dmose, parrt
tombu: dmose, kg9s
dmose: tombu
kg9s: dmose
"""

adj = adjlist(data)

nodenames = adj.keys()
expecting = ['parrt', 'tombu', 'dmose', 'kg9s']
if nodenames != expecting:
	print "error: expecting", expecting, "found", nodenames
chktargets('parrt', ['tombu', 'dmose', 'parrt'])
chktargets('tombu', ['dmose', 'kg9s'])
chktargets('dmose', ['tombu'])
chktargets('kg9s', ['dmose'])

A = adjmatrix(adj)
expecting = [[1, 1, 1, 0],
			 [0, 0, 1, 1],
			 [0, 1, 0, 0],
			 [0, 0, 1, 0]]
if A != expecting:
	print "error: expecting", expecting, "found", A

checknodes("parrt", ['parrt', 'tombu', 'dmose', 'kg9s'])
checknodes("tombu", ['tombu', 'dmose', 'kg9s'])
checknodes("dmose", ['tombu', 'dmose', 'kg9s'])
checknodes("kg9s", ['dmose', 'kg9s', 'tombu'])

dot = gendot(adj)
expecting = """digraph g {
  rankdir=LR;
  parrt -> tombu;
  parrt -> dmose;
  parrt -> parrt;
  tombu -> dmose;
  tombu -> kg9s;
  dmose -> tombu;
  kg9s -> dmose;
}
"""

if dot != expecting:
	print "error: invalid DOT"
