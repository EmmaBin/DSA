#Given the head of a linked list with an odd number of nodes head, 
#return the value of the node in the middle.

#For example, given a linked list that represents 1 -> 2 -> 3 -> 4 -> 5, return 3

#the difficulty in this problem comes from the fact that we don't know how long the linked list is


#method 1 
#iterate through the linked list once with a dummy pointer to find the length, 
#then iterate from the head again once we know the length to find the middle.

def get_middle(head):
    length = 0
    dummy = head
    while dummy:
        length += 1
        dummy = dummy.next
    
    for _ in range(length // 2):
        head = head.next
    
    return head.val

#method 2
#If we have one pointer moving twice as fast as the other, 
#then by the time it reaches the end, 
#the slow pointer will be halfway through since it is moving at half the speed.

def get_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.val

#The pointers use O(1)O(1) space, 
#and if there are nn nodes in the linked list, 
#the time complexity is O(n)O(n) for the traversals.
