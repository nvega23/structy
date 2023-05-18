# leaf list
# Write a function, leaf_list, that takes in the root of a binary tree and returns a list containing the values of all leaf nodes in left-to-right order.

# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

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

# leaf_list(a) # -> [ 'd', 'e', 'f' ]

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def leaf_list(root):
  if root is None:
    return []
  stack = [root]
  output = []
  while stack:
    node = stack.pop()
    if node.left is None and node.right is None:
      output.append(node.val)
    if node.right is not None:
      stack.append(node.right)
    if node.left is not None:
      stack.append(node.left)
  return output
