# insert node
# Write a function, insert_node, that takes in the head of a linked list, a value, and an index. The function should insert a new node with the value into the list at the specified index. Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.

# Do this in-place.

# You may assume that the input list is non-empty and the index is not greater than the length of the input list.

# test_00:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

# a.next = b
# b.next = c
# c.next = d

# # a -> b -> c -> d

# insert_node(a, 'x', 2)
# # a -> b -> x -> c -> d
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index):
  if index == 0:
    newHead = Node(value)
    newHead.next = head
    return newHead
  curr = head
  count = 0
  while curr is not None:
    if count == index - 1:
      temp = curr.next
      curr.next = Node(value)
      curr.next.next = temp
    count += 1
    curr = curr.next
  return head


