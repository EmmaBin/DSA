# Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

# Example

# For st = "abcdc", the output should be
# solution(st) = "abcdcba".

def solution(st):
    for i in range(len(st)):
        new_words = st+st[:i][::-1]
        if new_words == new_words[::-1]:
            return new_words