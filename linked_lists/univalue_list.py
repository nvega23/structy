# is univalue list
# Write a function, is_univalue_list, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list contains exactly one unique value.

# You may assume that the input list is non-empty.

# test_00:
# a = Node(7)
# b = Node(7)
# c = Node(7)

# a.next = b
# b.next = c

# # 7 -> 7 -> 7

# is_univalue_list(a) # True

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def is_univalue_list(head):
#   hash counting the nodes values
  curr = head
  count = {}
  while curr is not None:
    count[curr.val] = 1 + count.get(curr.val, 0)
    curr = curr.next
    if len(count) > 1:
      return False
  return True
