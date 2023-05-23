# has path
# Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.

# Hey. This is our first graph problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ

# graph = {
#   'f': ['g', 'i'],
#   'g': ['h'],
#   'h': [],
#   'i': ['g', 'k'],
#   'j': ['i'],
#   'k': []
# }

# has_path(graph, 'f', 'k') # True

def has_path(graph, src, dst):
  if src == dst:
    return True

  for node in graph[src]:
    if has_path(graph, node, dst) == True:
      return True
  return False
