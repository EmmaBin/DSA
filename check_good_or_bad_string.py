#https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

from collections import defaultdict
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)
        for i in s:
            counts[i] += 1

        reference = counts[s[0]]
        for key in counts:
            if counts[key] != reference:
                return False

        return True


from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        frequencies = counts.values()
        return len(set(frequencies)) == 1