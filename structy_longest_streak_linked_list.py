#Write a function, longest_streak,
#  that takes in the head of a linked list as an argument. 
# The function should return the length of the longest consecutive streak of the same value within the list.


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def longest_streak(head):
  max_result = 0
  curr_result = 0
  prev_val = None
  curr = head
  
  while curr is not None:
    if curr.val == prev_val:
      curr_result +=1
    else:
      curr_result =1
    prev_val = curr.val
    
    curr = curr.next
    max_result=max(max_result,curr_result)
  return max_result

      
    
#clarification: if head is none, return 0
#               if no head.next, return 1
#input: linked list, output: max len of consecutive value
#high level:
#    1. keep count of the len, one varaible to track
#    2. traverse the linked list and comparet all at once
#logic:
# initiate count =1, curr = head, prev = head
# while curr is not None:
    # curr = curr.next go to next one
    # if prev.val == curr.val: check value with previous one
          # count +=1 update count
    #temp = count 
    #else:
        #count = 1 reset count
        # count = max(temp, count)
  # return count


def longest_streak(head):

  if head is None:
    return 0
  if head.next is None:
    return 1
  
  count = 1
  prev = head
  curr=head.next
  result = 0
  while curr is not None:
    if curr.val == prev.val:
      count +=1
      prev=curr
      curr=curr.next
    else:
      result = max(count, result)
      count = 1
      prev = curr
      curr = curr.next
  result = max(count, result)
  return result