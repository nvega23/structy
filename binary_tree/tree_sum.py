# tree sum
# Write a function, treeSum, that takes in the root of a binary tree that contains number values. The function should return the total sum of all values in the tree.

# test_00:
# const a = new Node(3);
# const b = new Node(11);
# const c = new Node(4);
# const d = new Node(4);
# const e = new Node(-2);
# const f = new Node(1);

# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;

# //       3
# //    /    \
# //   11     4
# //  / \      \
# // 4   -2     1

# treeSum(a); // -> 21
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_sum(root):
  if root is None:
    return 0
  return root.val + tree_sum(root.left) + tree_sum(root.right)
