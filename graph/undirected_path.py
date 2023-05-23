# undirected path
# Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return a boolean indicating whether or not there exists a path between node_A and node_B.

# edges = [
#   ('i', 'j'),
#   ('k', 'i'),
#   ('m', 'k'),
#   ('k', 'l'),
#   ('o', 'n')
# ]

# undirected_path(edges, 'j', 'm') # -> True

def undirected_path(edges, node_A, node_B):
  graph = make_graph(edges)
  return get_path(graph, node_A, node_B, set())

def get_path(graph, src, dst, visited):
  if src == dst:
    return True
  if src in visited:
    return False
  visited.add(src)
  for neighbor in graph[src]:
    if get_path(graph, neighbor, dst, visited) == True:
      return True
  return False

def make_graph(edges):
  graph = {}
  for edge in edges:
    a,b = edge
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  return graph
