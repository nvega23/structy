# all tree paths
# Write a function, all_tree_paths, that takes in the root of a binary tree. The function should return a 2-Dimensional list where each subarray represents a root-to-leaf path in the tree.

# The order within an individual path must start at the root and end at the leaf, but the relative order among paths in the outer list does not matter.

# You may assume that the input tree is non-empty.

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

# all_tree_paths(a) # ->
# # [
# #   [ 'a', 'b', 'd' ],
# #   [ 'a', 'b', 'e' ],
# #   [ 'a', 'c', 'f' ]
# # ]

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def all_tree_paths(root):
  if root is None:
    return []
  if root.left is None and root.right is None:
    return [[root.val]]
  output = []

  sub_path_left = all_tree_paths(root.left)
  for sub in sub_path_left:
    output.append([root.val, *sub])
  sub_path_right = all_tree_paths(root.right)
  for sub in sub_path_right:
    output.append([root.val, *sub])

  return output

