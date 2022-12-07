#https://www.hackerrank.com/challenges/two-strings/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps


def twoStrings(s1, s2):
    s1_set = set(s1)
    s2_set= set(s2)
    result ='NO'
    for letter in s1_set:
        if letter in s2_set:
            result = 'YES'
            break
    return result

#use set and return not print