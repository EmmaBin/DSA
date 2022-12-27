#Given the head of a linked list and an integer k, return the kth 
#the node from the end.


#If we separate the two pointers by a gap of k, 
#and then move them at the same speed, 
#they will always be k apart. 
# When the fast pointer (the one further ahead) reaches the end, 
#then the slow pointer must be at the desired node, 
#since it is k nodes behind.

def find_node(head, k):
    slow = head
    fast = head
    for _ in range(k):
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow