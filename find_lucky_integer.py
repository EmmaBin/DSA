

def findLucky(self, arr: List[int]) -> int:
        large = -1
        unique = set(arr)
        for item in unique:
            count = arr.count(item)
            if item == count:
                large = max(large, item)              
        return large



from collections import defaultdict
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = defaultdict(int)
        result = -1
        for num in arr:
            counter[num]+=1
        for key, value in counter.items():
            if key == value:
                result = max(result, value)
  
        return result 