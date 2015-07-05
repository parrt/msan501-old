from graph import *

# test dot
g = \
"""
parrt: tombu, dmose, parrt
tombu: dmose, kg9s
dmose: tombu
kg9s: dmose
"""
list = adjlist(g)
dot = gendot(list)
print dot
