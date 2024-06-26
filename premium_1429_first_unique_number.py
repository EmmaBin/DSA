# You have a queue of integers, you need to retrieve the first unique integer in the queue.

# Implement the FirstUnique class:

# FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
# int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
# void add(int value) insert value to the queue.


# Example 1:

# Input:
# ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
# [[[2,3,5]],[],[5],[],[2],[],[3],[]]
# Output:
# [null,2,null,2,null,3,null,-1]
# Explanation:
# FirstUnique firstUnique = new FirstUnique([2,3,5]);
# firstUnique.showFirstUnique(); // return 2
# firstUnique.add(5);            // the queue is now [2,3,5,5]
# firstUnique.showFirstUnique(); // return 2
# firstUnique.add(2);            // the queue is now [2,3,5,5,2]
# firstUnique.showFirstUnique(); // return 3
# firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
# firstUnique.showFirstUnique(); // return -1


class Node:
    def __init__(self, val, next=None):
        # Ensure the node value is in list format
        self.val = [val]
        self.next = next


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.head = None
        self.tail = None
        self.val_map = {}  # To keep track of nodes for quick access

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        curr = self.head
        while curr:
            if len(curr.val) == 1:
                return curr.val[0]
            curr = curr.next
        return -1

    # O(1)

    def add(self, value: int) -> None:
        if value in self.val_map:
            # 找出那个node 【2，2，2】
            node = self.val_map[value]
            node.val.append(value)
        else:
            new_node = Node(value)
            self.val_map[value] = new_node
            if self.tail:
                self.tail.next = new_node
                self.tail = new_node
            else:
                self.head = new_node
                self.tail = new_node


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
