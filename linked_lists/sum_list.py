# sum list
# Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.

# test_00:
# a = Node(2)
# b = Node(8)
# c = Node(3)
# d = Node(-1)
# e = Node(7)

# a.next = b
# b.next = c
# c.next = d
# d.next = e

# # 2 -> 8 -> 3 -> -1 -> 7

# sum_list(a) # 19


def sum_list(head):
  curr = head
  output = 0
  while curr is not None:
    output += curr.val
    curr = curr.next
  return output
