#https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/


#below is a wrong answer,
#bcz input = [75,35,59,66,69,53,37,16,60,98,11,33,3,85,59,65,59,44,34,89,72,47]
#output is [75,69,53,37,16,60,98,11,3,85,44,89,72,47]
#expected output is [75,69,53,37,16,98,11,3,85,44,89,72,47]

#錯的原因是，先用hashmap把重複的數字59刪掉了， 但是60就漏掉了，所以不能先刪重複
def findLonely(self, nums: List[int]) -> List[int]:
    dict = {}
    result =[]
    keys=[]
    #use hashmap to create key(num):value(ocurrence) pair to rule out value >1 
    for num in nums:
        dict[num] = dict.get(num, 0) +1
    #get all the no repeated number into a list
    for key, value in dict.items():
        if value==1:
            keys.append(key)
    #convert a list to a set to improve cheking i O(1)
    new_set=set(keys)
    for num in keys:
        if (num+1 not in new_set) and (num-1 not in new_set):
            result.append(num)
    return result

#below is a working solution, check no adjacent numbers first 

def findLonely(self, nums: List[int]) -> List[int]:
    dict = {}
    result =[]
    new_set = set(nums)
    #create a set to check no adjacent nums first and then using hashmap
    #to filter out the numbers whose occurance is greater than 1 
    for num in nums:
        dict[num] = dict.get(num, 0) +1
    for num in nums:

        if (num+1 not in new_set) and (num-1 not in new_set):
            if dict[num] == 1:
                result.append(num)
    return result



#A more optimal way is using counter 

def findLonely(self, nums: List[int]) -> List[int]:
    counts = Counter(nums)
    
    ans = []
    for x in nums:
        if counts[x] == 1 and x - 1 not in counts and x + 1 not in counts:
            ans.append(x)
    return ans