from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        dic = Counter(hand)
        sorted_keys = sorted(dic.keys())
        for key in sorted_keys:
            if dic[key] > 0:
                start_count = dic[key]
                for i in range(key, key+groupSize):
                    if start_count > dic[i]:
                        return False
                    dic[i] -= start_count

        return True
