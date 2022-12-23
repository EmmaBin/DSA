#https://leetcode.com/problems/find-players-with-zero-or-one-losses/

#sorted(lst), return a sorted list. append to list, append 什麼就是什麼，append一個list
#裏面就是list


from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #understanding the question:
        #[winer, loser] whoever goes first is winner, each integer is a player itself
        #return two lists inside a list
        #[    [position alway at i[0]],    [only at i[1]once]     ]
        # return in increasing order
        #hint: Count the number of times a player loses while iterating through the matches.
        counts = defaultdict(int)
        no_lost =[]
        lost_once = []
        ans=[]
        for lst in matches:
            counts[lst[1]] +=1
            counts[lst[0]] += 0

        
        for key in counts:
            if counts[key] == 0:
                no_lost.append(key)

            if counts[key] == 1:
                lost_once.append(key)
        ans.append(sorted(no_lost))
        ans.append(sorted(lost_once))
        return ans


class Solution: 
    def findWinners(self, matches : List[List[int]]) ->List[List[int]]: 
        seen = set() losses_count = {}
        
        for winner, loser in matches:
            seen.add(winner)
            seen.add(loser)
            losses_count[loser] = losses_count.get(loser, 0) + 1
        
        #Add players with 0 or 1 loss to the corresponding list.
        zero_lose, one_lose = [], []
        for player in seen:

            #get() method returns the value of the item with the specified key.

            #second parameter is optional, 
            #A value to return if the specified key does not exist.
            count = losses_count.get(player, 0)
            if count == 0:
                zero_lose.append(player)
            elif count == 1:
                one_lose.append(player)
        
        return [sorted(zero_lose), sorted(one_lose)]
#Time complexity: O(n⋅log⁡n), space is O(n)





    #method 2: using set, 不是推薦的方法
    #Time complexity: O(n⋅log⁡n)

# For each match from matches, 
# we have up to 3 operations on these sets. 
# Operations on hash set require O(1) time. 
# Thus the iteration over matches takes O(n)time.
# We need to store two kinds of players in two arrays and sort them. 
# In the worst-case scenario, there may be O(n) players in these arrays, 
# thus it requires O(n⋅log⁡n) time.
# To sum up, the time complexity is O(n⋅log⁡n)
# space is 0(n)

def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    zero_loss = set()
    one_loss = set()
    more_losses = set()

for winner, loser in matches:
    # Add winner
    if (winner not in one_loss) and (winner not in more_losses):
        zero_loss.add(winner)
    # Add or move loser.
    if loser in zero_loss:
        zero_loss.remove(loser)
        one_loss.add(loser)
    elif loser in one_loss:
        one_loss.remove(loser)
        more_losses.add(loser)
    elif loser in more_losses:
        continue
    else:
        one_loss.add(loser)          
    
return [sorted(list(zero_loss)), sorted(list(one_loss))]


#method 3 

class Solution: 
    def findWinners(self, matches: List[List[int]]) ->List[List[int]]: 
        losses_count = {}
        
        for winner, loser in matches:
            losses_count[winner] = losses_count.get(winner, 0)
            losses_count[loser] = losses_count.get(loser, 0) + 1
        
        zero_lose, one_lose = [], []
        for player, count in losses_count.items():
            if count == 0:
                zero_lose.append(player)
            if count == 1:
                one_lose.append(player)
        
        return [sorted(zero_lose), sorted(one_lose)]

# Time complexity: O(n⋅log⁡n) Space: O(n)