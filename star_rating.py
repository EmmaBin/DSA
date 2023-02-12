#Have the function StarRating(str) take the str parameter being passed which will be an average rating between 0.00 and 5.00, 
# and convert this rating into a list of 5 image names to be displayed in a user interface to represent the rating as a list of stars and half stars. 
# Ratings should be rounded to the nearest half. There are 3 image file names available: "full.jpg", "half.jpg", "empty.jpg". 
# The output will be the name of the 5 images (without the extension), from left to right, separated by spaces. 
# For example: if str is "2.36" then this should be displayed by the following image:


def StarRating(strParam):

  result = ''
  ones = int(strParam[0])
  number = float(strParam)
  decimal = number - int(number)
  
  if decimal >= 0.75:
    result = 'full ' * (ones +1) + 'empty '* (4-ones)
  elif decimal >= 0.25 and decimal < 0.75:
    result = 'full ' * ones + 'half ' + 'empty ' * (4 - ones)
  else:
    result ='full ' * ones + 'empty ' * (5-ones)
  
  return result

# keep this function call here 
print(StarRating(input()))