# merge lists
# Write a function, merge_lists, that takes in the head of two sorted linked lists as arguments. The function should merge the two lists together into single sorted linked list. The function should return the head of the merged linked list.

# Do this in-place, by mutating the original Nodes.

# You may assume that both input lists are non-empty and contain increasing sorted numbers.

# test_00:
# a = Node(5)
# b = Node(7)
# c = Node(10)
# d = Node(12)
# e = Node(20)
# f = Node(28)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# # 5 -> 7 -> 10 -> 12 -> 20 -> 28

# q = Node(6)
# r = Node(8)
# s = Node(9)
# t = Node(25)
# q.next = r
# r.next = s
# s.next = t
# # 6 -> 8 -> 9 -> 25

# merge_lists(a, q)
# # 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_lists(head_1, head_2):
  curr = head_1
  curr2 = head_2
  dummy_node = Node(None)
  tail = dummy_node
  while curr is not None and curr2 is not None:
    if curr.val < curr2.val:
      tail.next = curr
      curr = curr.next
    else:
      tail.next = curr2
      curr2 = curr2.next
    tail = tail.next
  if curr is not None:
    tail.next = curr
  if curr2 is not None:
    tail.next = curr2
  return dummy_node.next
  