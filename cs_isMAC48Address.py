# A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

# The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

# Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

# Example

# For inputString = "00-1B-63-84-45-E6", the output should be
# solution(inputString) = true;
# For inputString = "Z1-1B-63-84-45-E6", the output should be
# solution(inputString) = false;
# For inputString = "not a MAC-48 address", the output should be
# solution(inputString) = false.


import re
def solution(inputString):
   pt = re.compile('^[a-fA-F0-9]{2}$')
   lst = inputString.split('-')
   if len(lst) != 6:
      return False
   for ch in lst:
      if not pt.match(ch):
         return False
   return True