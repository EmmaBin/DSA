#Have the function CountingMinutesI(str) take the str parameter being passed which will be two times (each properly formatted with a colon and am or pm) 
# separated by a hyphen and return the total number of minutes between the two times. 
# The time will be in a 12 hour clock format. For example: if str is 9:00am-10:00am then the output should be 60. If str is 1:00pm-11:00am the output should be 1320.


def convert_to_24hrs(time):
  #in a time string, if last two digits are am: return as it is
  

  if time[-2] == 'a':
    return time[:-2]
  else:
    
    new_time= time.split(':')
    if new_time[0] == '12' and int(new_time[-1][:2])>0:
      result = f"0:{new_time[-1]}"
    else:
      hours = int(new_time[0])+12
      result = f"{hours}:{new_time[-1]}"
  
  return result[:-2]

def convert_to_minutes(time):

  time_list = time.split(':')
  result = int(time_list[0]) * 60 + int(time_list[1])
  return result


def CountingMinutesI(strParam):
  time_list = strParam.split('-')
  time1 = convert_to_24hrs(time_list[0])
  time2 = convert_to_24hrs(time_list[-1])
  time1_mins = convert_to_minutes(time1)
  time2_mins = convert_to_minutes(time2)
  if time1_mins < time2_mins:
    result = time2_mins - time1_mins
  else:
    result = 24*60 - (time1_mins - time2_mins)
  
  

  # code goes here
  return result

# keep this function call here 
print(CountingMinutesI(input()))