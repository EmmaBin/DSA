#Have the function BinaryReversal(str) take the str parameter being passed, 
# which will be a positive integer, 
# take its binary representation (padded to the nearest N * 8 bits),
#  reverse that string of bits, and then finally return the new reversed string in decimal form. 
# For example: if str is "47" then the binary version of this integer is 101111 but we pad it to be 00101111. 
# Your program should reverse this binary string which then becomes: 11110100 and then finally return the decimal version of this string, which is 244.

def BinaryReversal(str):

  # Convert String to int
  input_int = int(str)

  # Convert int to binary string
  input_bin = format(input_int, 'b')

  # Ensure binary string is padded to the nearest N*8 bits
  while len(input_bin)%8 != 0:
    input_bin = "0" + input_bin

  # Reverse binary string by slicing backwards each character
  input_rev = input_bin[::-1]

  # Convert back to int for output
  res = int(input_rev, 2)

  return res

# keep this function call here 
print(BinaryReversal(input()))