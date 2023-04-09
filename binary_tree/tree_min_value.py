# tree min value
# Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. The function should return the minimum value within the tree.

# You may assume that the input tree is non-empty.

# test_00:
# a = Node(3)
# b = Node(11)
# c = Node(4)
# d = Node(4)
# e = Node(-2)
# f = Node(1)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #       3
# #    /    \
# #   11     4
# #  / \      \
# # 4   -2     1
# tree_min_value(a) # -> -2
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_min_value(root):
  if root is None:
    return float("inf")
  smallestLeft = tree_min_value(root.left)
  smallestRight = tree_min_value(root.right)
  return min(root.val, smallestLeft, smallestRight)
