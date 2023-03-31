# get node value
# Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.

# If there is no node at the given index, then return None.

# test_00:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")

# a.next = b
# b.next = c
# c.next = d

# # a -> b -> c -> d

# get_node_value(a, 2) # 'c'
def get_node_value(head, index):
  curr = head
  i = 0
  while curr is not None:
    if i == index:
      return curr.val
    i += 1
    curr = curr.next
