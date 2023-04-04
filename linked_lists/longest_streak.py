# longest streak
# Write a function, longest_streak, that takes in the head of a linked list as an argument. The function should return the length of the longest consecutive streak of the same value within the list.

# test_00:
# a = Node(5)
# b = Node(5)
# c = Node(7)
# d = Node(7)
# e = Node(7)
# f = Node(6)

# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f

# # 5 -> 5 -> 7 -> 7 -> 7 -> 6

# longest_streak(a) # 3
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def longest_streak(head):
  maxS = 0
  streak = 0
  prevVal = None
  curr = head
  while curr is not None:
    if curr.val == prevVal:
      streak += 1
    else:
      streak = 1
    prevVal = curr.val
    if maxS < streak:
      maxS = streak
    curr = curr.next
  return maxS
