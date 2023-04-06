# breadth first values
# Write a function, breadth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in breadth-first order.

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

# breadth_first_values(a)
# #    -> ['a', 'b', 'c', 'd', 'e', 'f']
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def breadth_first_values(root):
  if root is None:
    return []
  output = []
  stack = [root]
  while stack:
    node = stack.pop()
    output.append(node.val)
    if node.left:
      stack.append(node.left)
    if node.right:
      stack.append(node.right)
  return output
