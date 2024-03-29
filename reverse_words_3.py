#https://leetcode.com/problems/reverse-words-in-a-string-iii/

#Given a string s, 
#reverse the order of characters in each word within a sentence
#while still preserving whitespace and initial word order.

#Input: s = "Let's take LeetCode contest"
#Output: "s'teL ekat edoCteeL tsetnoc"


#high level:
#1. convert to list using split method, empty space as a delimiter
#2. reverse the whole list using slicing [::-1] => ['contest', 'LeetCode', 'take', "Let's"]
#3. use join method to convert it back to string => contest LeetCode take Let's
#4. reverse the whole string now => s'teL ekat edoCteeL tsetnoc

#Time and Space Complexity???

class Solution:
    def reverseWords(self, s: str) -> str:

        return " ".join(s.split(" ")[::-1])[::-1]


#method2: save it in a new list and then join back as string to return O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        answer=[]
        s_list = s.split(' ')
        for i in s_list:
            new_i= i[::-1]
            answer.append(new_i)
        return ' '.join(answer)


# method3: two pointers

#1.convert the whole string into list
#2. loop over the list, initiate two pointers, left starts at 0, right starts at the last index
#3. in order to switch the position, we also need to convert each string in the lIST as a list so later can be operated on
#4. advance the two pointers until the condition met which is the left and right almost meet each other
#5. after each loop/each list inside the list, we need to reassign that word at the same index using join method to convert back to string
#6. after everything has been converted inside the list, we need to convert the list back to string, remember the delimiter is empty space

class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(' ')
        for i in range(len(s_list)):
            left=0
            right=len(s_list[i])-1

            temp=list(s_list[i])
            while right >left:
                temp[left], temp[right] = temp[right], temp[left]
                right -=1
                left +=1
            s_list[i] = ''.join(temp)
        return ' '.join(s_list)

  #二刷
  #以下是错误的：
  class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(' ')
        result =[]
        for word in s_list:
            left =0
            right= len(word)-1
            while right > left:
                temp = list(word)
                temp[left], temp[right] = temp[right], temp[left]
                left+=1
                right-=1
            #这个是错的，因为join的不应该是word, word,还是原来的string
            result.append(''.join(word))
        return (' '.join(result))
#这个也是错的

class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(' ')
        result =[]
        for word in s_list:
            left =0
            right= len(word)-1
            while right > left:
                temp = list(word)
                temp[left], temp[right] = temp[right], temp[left]
                left+=1
                right-=1
                
            result.append(''.join(temp))
        return (' '.join(result))
"God Ding"  --> "doG Dnig"  应该是 "doG gniD"

#这个是正确的：
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(' ')
        result =[]
        for word in s_list:
            left =0
            right= len(word)-1
            #如果把temp放在while loop 里面，那每一次temp 都是同一个word, 而pointers在变，所以只有最后一次变化
            #在出来while loop 时候 被记住了
            temp = list(word)
            while right > left:
                
                temp[left], temp[right] = temp[right], temp[left]
                left+=1
                right-=1
                
    
            result.append(''.join(temp))
        return (' '.join(result))
