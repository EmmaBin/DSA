#Have the function StarRating(str) take the str parameter being passed which will be an average rating between 0.00 and 5.00, 
# and convert this rating into a list of 5 image names to be displayed in a user interface to represent the rating as a list of stars and half stars. 
# Ratings should be rounded to the nearest half. There are 3 image file names available: "full.jpg", "half.jpg", "empty.jpg". 
# The output will be the name of the 5 images (without the extension), from left to right, separated by spaces. 
# For example: if str is "2.36" then this should be displayed by the following image:


def StarRating(str):
  n_fulls = int(float(str) // 1)
  remainer = float(str) - n_fulls

  if remainer < 0.25:
    n_halfs = 0
  elif remainer < 0.75:
    n_halfs = 1
  else:
    n_halfs = 0
    n_fulls += 1

  n_empties = 5 - n_fulls - n_halfs

  ans = ''
  for i in range(n_fulls):
    ans += 'full '
  
  if n_halfs == 1:
    ans += 'half '
  
  for i in range(n_empties):
    ans += 'empty '
  
  return ans[:-1]
# keep this function call here 
print(StarRating(input()))