# max root to leaf path sum
# Write a function, max_path_sum, that takes in the root of a binary tree that contains number values. The function should return the maximum sum of any root to leaf path within the tree.

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

# max_path_sum(a) # -> 18

def max_path_sum(root):
  if root is None:
    return float("-inf")
  if root.left is None and root.right is None:
    return root.val
  return root.val + max(max_path_sum(root.left), max_path_sum(root.right))
