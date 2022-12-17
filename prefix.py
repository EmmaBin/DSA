#Given an integer array nums, 
#an array queries where queries[i] = [x, y] and an integer limit,
#return a boolean array that represents the answer to each query.
#A query is true if the sum of the subarray from x to y is less than limit, 
#or false otherwise.

def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    
    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)

    return ans