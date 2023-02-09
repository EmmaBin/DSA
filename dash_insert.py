#Have the function DashInsert(str) insert dashes ('-') between each two odd numbers in str. 
#For example: if str is 454793 the output should be 4547-9-3. Don't count zero as an odd number.

def DashInsert(strParam):
  new_list = list(strParam)
  for i in range(len(new_list)-1):
    if int(new_list[i]) % 2!=0 and int(new_list[i+1]) % 2 !=0:
      temp= new_list[i] + '-'
      new_list[i] = temp



  # code goes here
  return ''.join(new_list)

# keep this function call here 
print(DashInsert(input()))