class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        result = []
        for i, size in enumerate(groupSizes):

            if size not in d:
                d[size] = []

            d[size].append(i)
            if len(d[size]) == size:
                result.append(d[size])
                d[size] = []

        return result
