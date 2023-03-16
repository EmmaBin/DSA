#https://leetcode.com/problems/last-stone-weight/description/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) ==1:
            return stones[0]
        while len(stones) >1:
            stones = sorted(stones)[::-1]
            print(stones)
            if stones[0] == stones[1]:
                stones=stones[2:]
            else:
                new_stone=stones[0]-stones[1]
                stones = stones[2:]
                stones.append(new_stone)
        if len(stones)>0:
            return stones[0]
        else:
            return 0