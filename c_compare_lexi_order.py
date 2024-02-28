# Given two strings s and t, both consisting of lowercase English letters and digits, your task is to calculate how many ways exactly one digit could be removed from one of the strings so that s is lexicographically smaller than t after the removal. Note that we are removing only a single instance of a single digit, rather than all instances (eg: removing 1 from the string a11b1c could result in a1b1c or a11bc, but not abc).

# Also note that digits are considered lexicographically smaller than letters.


def solution(s, t):
    counter =0
    s_list = list(s)
    t_list = list(t)
    pt1=0
    new_s_list = s_list
    new_t_list = t_list
    for i, c in enumerate(s_list):
        if c.isdigit():
            new_s_list=s_list[:i]+s_list[i+1:]
            if compare_strings(("").join(new_s_list),t):
                counter+=1
    for i,c in enumerate(t_list):
        if c.isdigit():
            new_t_list=t_list[:i]+t_list[i+1:]
            if compare_strings(s,("").join(new_t_list)):
                counter+=1 
    return counter
def compare_strings(s,t):
    return s<t