# Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

# Example

# For text = "Ready, steady, go!", the output should be
# solution(text) = "steady".

def solution(text):
    print(re.split("[^a-zA-Z]", text))
    return max(re.split("[^a-zA-Z]", text), key=len)