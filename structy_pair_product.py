# Write a function, pair_product, that takes in a list and a target product as arguments. 
#The function should return a tuple containing a pair of indices whose elements multiply to the given target. 
#The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair whose product is the target

def pair_product(numbers, target_product):
  dict = {}
  for index, number in enumerate(numbers):
    divident = target_product//number
    if divident in dict:
      return(index, dict[divident])
    dict[number] = index