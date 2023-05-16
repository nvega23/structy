# tree levels
# Write a function, tree_levels, that takes in the root of a binary tree. The function should return a 2-Dimensional list where each sublist represents a level of the tree.

# test_00:
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f

# tree_levels(a) # ->
# # [
# #   ['a'],
# #   ['b', 'c'],
# #   ['d', 'e', 'f']
# # ]

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_levels(root):
  if root is None:
    return []
  stack = [(root, 0)]
  output = []
  while stack:
    node, level = stack.pop()
    if len(output) == level:
      output.append([node.val])
    else:
      output[level].append(node.val)

    if node.right is not None:
      stack.append([node.right, level + 1])

    if node.left is not None:
      stack.append([node.left, level + 1])

  return output
