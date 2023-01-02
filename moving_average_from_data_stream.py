#https://leetcode.com/problems/moving-average-from-data-stream/

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue=collections.deque()
        self.total =0
        

    def next(self, val: int) -> float:
        self.queue.appendleft(val)
        self.total += val
        if len(self.queue) > self.size:
            removed = self.queue.pop()
            self.total -= removed
        return self.total/len(self.queue)


#next is O(1)

#reference about dequeue https://www.geeksforgeeks.org/deque-in-python/