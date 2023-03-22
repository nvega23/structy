# anagrams
# Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.

# test_00:
# anagrams('restful', 'fluster') # -> True

def anagrams(s1, s2):
  count1 = {}
  count2 = {}

  for char in s1:
    count1[char] = 1 + count1.get(char, 0)
  for char in s2:
    count2[char] = 1 + count2.get(char, 0)
  return count1 == count2

print(anagrams('restful', 'fluster')) # -> True
