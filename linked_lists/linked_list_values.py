# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_values(head):
  curr = head
  output = []
  while curr is not None:
    output.append(curr.val)
    curr = curr.next
  return output
