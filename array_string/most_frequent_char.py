# most frequent char
# Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

# You can assume that the input string is non-empty.

# test_00:
# most_frequent_char('bookeeper') # -> 'e'

def most_frequent_char(s):
  count = {}
  for char in s:
    count[char] = 1 + count.get(char, 0)

  best = None
  for char in s:
    if best is None or count[char] > count[best]:
      best = char
  return best
