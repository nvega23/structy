# compress
# Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'
# You can assume that the input only contains alphabetic characters.

# test_00:
# compress('ccaaatsss') # -> '2c3at3s'

def compress(s):
  s += "!"
  output = []
  i = 0
  j = 0
  while j < len(s):
    if s[i] == s[j]:
      j += 1
    else:
      nums = j - i
      if nums == 1:
        output.append(s[i])
      else:
        output.append(str(nums))
        output.append(s[i])
      i = j
  return "".join(output)
