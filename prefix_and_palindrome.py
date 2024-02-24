# You are given a string s. Consider the following algorithm applied to this string:

# Take all the prefixes of the string, and choose the longest palindrome between them.
# If this chosen prefix contains at least two characters, cut this prefix from s and go back to the first step with the updated string. Otherwise, end the algorithm with the current string s as a result.
# Your task is to implement the above algorithm and return its result when applied to string s.

# Note: you can click on the prefixes and palindrome words to see the definition of the terms if you're not familiar with them.

# Example

# For s = "aaacodedoc", the output should be solution(s) = "".

# The initial string s = "aaacodedoc" contains only three prefixes which are also palindromes - "a", "aa", "aaa". The longest one between them is "aaa", so we cut it from s.
# Now we have string "codedoc". It contains two prefixes which are also palindromes - "c" and "codedoc". The longest one between them is "codedoc", so we cut it from the current string and obtain the empty string.
# Finally the algorithm ends on the empty string, so the answer is "".
# For s = "codesignal", the output should be solution(s) = "codesignal".
# The initial string s = "codesignal" contains the only prefix, which is also palindrome - "c". This prefix is the longest, but doesn't contain two characters, so the algorithm ends with string "codesignal" as a result.

# For s = "", the output should be solution(s) = "".



def solution(s):
    #select prefixes-> substring
    #choose longest panlindrome
    # while prefixed panlindrom longer than 2, cut from sched
    # then repeat the process until nothing or return s 
    
    #find the longest subarray staring with s[0] can be panlindrome
    curr_len = len(find_longest_prefix(s))
    if curr_len ==1:
            return s

    while curr_len>=2:
        
        new_s = s[curr_len:]

        curr_len = len(find_longest_prefix(new_s))
        if curr_len ==1:
            return new_s
        s= new_s
    else:
        return ""

def find_longest_prefix(s):
    prefix=""
    temp=[]
    #aba
    for i in range(len(s)):
        temp.append(s[i])
        if temp ==temp[::-1]:
            prefix = "".join(temp)
    print(prefix)
    
    return prefix
     