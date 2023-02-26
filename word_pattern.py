#https://leetcode.com/problems/word-pattern/description/

def wordPattern(self, pattern: str, s: str) -> bool:

    
        words = s.split(" ")
        l_to_w_map = {} #letter to word mapping
        w_to_l_map = {} #word to letter mapping
        
        if len(pattern) != len(words): 
            
            return False
        for index, letter in enumerate(pattern):
            if letter in l_to_w_map:
                if l_to_w_map[letter] != words[index]:
                    return False
            else: 
                #check if the word already maps to a letter
                if words[index] in w_to_l_map:
                    return False
                else: # record new mapping
                    l_to_w_map[letter] = words[index]
                    w_to_l_map[words[index]] = letter
        return True

def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(pattern) != len(s) or len(set(s)) != len(set(pattern)):
            return False
        hash_map = {}
        for char in range(len(pattern)):
            if pattern[char] not in hash_map:
                hash_map[pattern[char]] = s[char]
            elif hash_map[pattern[char]] != s[char]:
                return False
        return True
