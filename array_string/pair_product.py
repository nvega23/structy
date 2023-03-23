# pair product
# Write a function, pair_product, that takes in a list and a target product as arguments. The function should return a tuple containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair whose product is the target.

# test_00:
# pair_product([3, 2, 5, 4, 1], 8) # -> (1, 3)

def pair_product(numbers, target_product):
  for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
      if numbers[i] * numbers[j] == target_product:
        return (i, j)
