def uncompress(s):
  i = 0
  j = 0
  output = []
  numbers = "0123456789"
  while j < len(s):
    if s[j] in numbers:
      j += 1
    else:
      num = int(s[i:j])
      output.append(s[j] * num)
      j += 1
      i = j
  return "".join(output)

print(uncompress("2c3a1t"))
