#https://leetcode.com/problems/check-if-the-sentence-is-pangram/

def checkIfPangram(self, sentence: str) -> bool:
    new_set = set(sentence)
    if len(new_set) < 26:
        return False
    else:
        return True



# method 2
def checkIfPangram(self, sentence: str) -> bool:
    # We iterate over 'sentence' for 26 times, one for each letter 'curr_char'.
    for i in range(26):
        curr_char = chr(ord('a') + i)

        # If 'sentence' doesn't contain 'curr_char', it is not a pangram.
        if sentence.find(curr_char) == -1:
            return False
    
    # If we manage to find all 26 letters, it is a pangram.
    return True


#method 3
def checkIfPangram(self, sentence: str) -> bool:
    # Array 'seen' of size 26.
    seen = [False] * 26

    # For every letter 'currChar', we find its ASCII code, 
    # and update value at the mapped index as true.
    for curr_char in sentence:
        seen[ord(curr_char) - ord('a')] = True
    
    # Once we finish iterating, check if 'seen' contains false.
    for status in seen:
        if not status:
            return False
    return True