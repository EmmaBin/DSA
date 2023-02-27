#Have the function TimeDifference(strArr) read the array of strings stored in strArr which will be an unsorted list of times in a twelve-hour format 
#like so: HH:MM(am/pm). 
# Your goal is to determine the smallest difference in minutes between two of the times in the list. 
#For example: if strArr is ["2:10pm", "1:30pm", "10:30am", "4:42pm"] 
# then your program should return 40 because the smallest difference is between 1:30pm and 2:10pm with a difference of 40 minutes. 
# The input array will always contain at least two elements and all of the elements will be in the correct format and unique.

def TimeDifference(strArr):
  def clockToAbsolute(clockTime):
    hourStr, minStrAmPm = clockTime.split(":")
    if hourStr != "12":
      hours = int(hourStr)  
    else:
      hours = 0
      
    minutes = int(minStrAmPm[:2])
    if minStrAmPm[2:] == "am":
      isAm = True
    else:
      isAm = False
    
    if isAm:
      return 60 * hours + minutes 
    else:
      return 60 * hours + minutes +  60 * 12

  absoluteTimes = sorted(clockToAbsolute(time) for time in strArr)
  print(absoluteTimes)
  timeDiffs = [absoluteTimes[i] - absoluteTimes[i-1] for i in range(1,len(absoluteTimes))]
  print(timeDiffs)

  timeDiffs.append(24 * 60 - absoluteTimes[-1] + absoluteTimes[0])
  print(timeDiffs)

  return min(timeDiffs) 
print(TimeDifference(["10:00am", "11:45pm", "5:00am", "12:01am"]))