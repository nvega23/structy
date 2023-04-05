# add lists
# Write a function, add_lists, that takes in the head of two linked lists, each representing a number. The nodes of the linked lists contain digits as values. The nodes in the input lists are reversed; this means that the least significant digit of the number is the head. The function should return the head of a new linked listed representing the sum of the input lists. The output list should have its digits reversed as well.

# Say we wanted to compute 621 + 354 normally. The sum is 975:

#    621
#  + 354
#  -----
#    975

# Then, the reversed linked list format of this problem would appear as:

#     1 -> 2 -> 6
#  +  4 -> 5 -> 3
#  --------------
#     5 -> 7 -> 9
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def add_lists(head_1, head_2, carry = 0):
  if head_1 is None and head_2 is None and carry == 0:
    return None
  val1 = 0 if head_1 is None else head_1.val
  val2 = 0 if head_2 is None else head_2.val
  sum = val1 + val2 + carry
  nextXarry = 1 if sum > 9 else 0
  digits = sum % 10

  result = Node(digits)

  next1 = None if head_1 is None else head_1.next
  next2 = None if head_2 is None else head_2.next

  result.next = add_lists(next1, next2, nextXarry)
  return result
