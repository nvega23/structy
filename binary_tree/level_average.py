# level averages
# Write a function, levelAverages, that takes in the root of a binary tree that contains number values. The function should return an array containing the average value of each level.

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

# levelAverages(a); // -> [ 3, 7.5, 1 ]

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def level_averages(root):
  if root is None:
    return []
  output = []
  stack = [(root, 0)]
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
  res = []
  for num in output:
    res.append(sum(num) / len(num))
  return res
