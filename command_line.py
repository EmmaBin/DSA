#Command Line
#Have the function CommandLine(str) take the str parameter being passed which represents the parameters given to a command in an old PDP system. 
# The parameters are alphanumeric tokens (without spaces) followed by an equal sign and by their corresponding value. 
# Multiple parameters/value pairs can be placed on the command line with a single space between each pair. 
# Parameter tokens and values cannot contain equal signs but values can contain spaces. 
# The purpose of the function is to isolate the parameters and values to return a list of parameter and value lengths. 
# It must provide its result in the same format and in the same order by replacing each entry (tokens and values) by its corresponding length.

#For example, if str is: "SampleNumber=3234 provider=Dr. M. Welby patient=John Smith priority=High" then your function should return the string "12=4 8=12 7=10 8=4" 
# because "SampleNumber" is a 12 character token with a 4 character value ("3234") followed by "provider" which is an 8 character token followed by a 12 character value ("Dr. M. Welby"), etc.


import re


def CommandLine(s):
  m = re.findall(r'([A-Za-z]+)=(?:([^=]+)(?=(?:[ ]+|$)))*', s)
  return ' '.join(f'{len(k)}={len(v)}' for k,v in m)
    

# keep this function call here 
print(CommandLine(input()))

def CommandLine(strParam):

  # code goes here
  str_P = strParam.split("=")
  tmp=''
  tmp += str(len(str_P[0])) + "="

  for i in str_P[1:-1]:
    v = i.rfind(" ")
    tmp += str(len(i[:v])) + " " + str(len(i[v+1:])) + "="

  tmp += str(len(str_P[-1]))
  return tmp

# keep this function call here 
print(CommandLine(input()))