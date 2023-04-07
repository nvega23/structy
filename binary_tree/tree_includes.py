# tree includes
# Write a function, tree_includes, that takes in the root of a binary tree and a target value. The function should return a boolean indicating whether or not the value is contained in the tree.

# test_00:
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

# tree_includes(a, "e") # -> True

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_includes(root, target):
  if root is None:
    return False
  output = []
  stack = [root]
  while stack:
    node = stack.pop()
    output.append(node.val)
    if node.left:
      stack.append(node.left)
    if node.right:
      stack.append(node.right)
  return target in output
