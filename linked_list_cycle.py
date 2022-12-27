#https://leetcode.com/problems/linked-list-cycle/

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

#This approach gives us a time complexity of O(n) and a space complexity of O(1), 
#where n is the number of nodes in the linked list


#method 2
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

#O(n) space

# The hashing solution: if you continuously iterate using the next pointer, there are two possibilities:

# If the linked list doesn't have a cycle, you will eventually reach null and finish.
# If the linked list has a cycle, you will eventually visit a node twice. We can use a set to detect this.