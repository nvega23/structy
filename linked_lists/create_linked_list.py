# create linked list
# Write a function, create_linked_list, that takes in a list of values as an argument. The function should create a linked list containing each item of the list as the values of the nodes. The function should return the head of the linked list.

# test_00:
# create_linked_list(["h", "e", "y"])
# # h -> e -> y
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def create_linked_list(values):
  head = Node(None)
  curr = head
  for char in values:
    curr.next = Node(char)
    curr = curr.next
  return head.next
    