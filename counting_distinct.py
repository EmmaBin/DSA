#You are given a string s and an integer k. 
#Find the length of the longest substring that contains at most k distinct characters.

#For example, given s = "eceba" and k = 2, return 3. 
#The longest substring with at most 2 distinct characters is "ece".

#method 1 - sliding window, find where is the violation
def find_longest(string_input, k):
  count = left= 0
  new_sub=''
  for right in range(len(string_input)):
    new_sub += string_input[right]
    while len(set(new_sub)) >k:
      left+=1
      #use string slicing to get rid of the first character
      new_sub=new_sub[1:]

     #update the count  
    count = max(count, right-left+1)


  return count

print(find_longest('eceba', 2))

#method 2 - sliding window and hashmap(should always be k pair inside the hashmap)

from collections import defaultdict
def find_longest_substring(s, k):
    counts = defaultdict(int)
    left = ans = 0
    for right in range(len(s)):
        counts[s[right]] += 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        
        ans = max(ans, right - left + 1)
    
    return ans

#The hash map occupies O(k)space, 
#as the algorithm will delete elements from the hash map once it grows beyond k