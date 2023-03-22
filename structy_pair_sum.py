#Write a function, pair_sum, that takes in a list and a target sum as arguments. 
# The function should return a tuple containing a pair of indices whose elements sum 
# to the given target. The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair that sums to the target.

def pair_sum(numbers, target_sum):
  dict ={}
  for index, number in enumerate(numbers):
    other_number = target_sum-number
    if other_number in dict:
      return (index, dict[other_number])
    dict[number] = index