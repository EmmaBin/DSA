class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def remove_node(head, target_val):
  #edge case: if head.val == target_val: return head.next, then prev pointer 就不好使了，还是直接return head.next
  #what if remove tail, 也是可以的
  if head.val == target_val:
    return head.next
  prev=Node(None)
  curr = head
  
  while curr is not None:
    if curr.val == target_val:
      prev.next= curr.next
      #the reason we break here is bcz we only want to find the first occurance
      break
    prev = curr
    curr=curr.next
  return head
  #while curr is not None:
    #traverse the linked list by updating curr value
    #check value 
      #if mathces:
        #prev.next=curr.next
        #break
      # prev=curr
      # curr=curr.next
  #return head