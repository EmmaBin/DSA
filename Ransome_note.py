#https://www.hackerrank.com/challenges/ctci-ransom-note/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

#create a look_up dictionary 

def checkMagazine(magazine, note):
    m_dict={}
    for letter in magazine:
        m_dict[letter] = m_dict.get(letter, 0)+1
    for letter in note:
        if letter not in m_dict.keys():
            print('No')
            return
        else:
            m_dict[letter] -=1
            if m_dict[letter]<0:
                print('No')
                return
    print('Yes')
    