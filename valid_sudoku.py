#https://leetcode.com/problems/valid-sudoku/description/

#check three conditons need to be true, return true
#for each subarr, either "." or 1-9 no duplicates
#each subarr is same length, so for same index in each subarr, same rule
# sub-boxes, for i in range(3), for j in range(3), check condition
#how to check condition, if number>9 return False, if not. save to a set,
#if already exist in the set, return False. 
#we need nested list many times
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for _ in range(9)]
        block = [[set() for _ in range(3)] for _ in range(3)]
        print(block)
        print(rows)
        print(cols)

        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == '.':
                    continue
                if (curr in rows[i]) or (curr in cols[j]) or (curr in block[i // 3][j // 3]):
                    return False
                rows[i].add(curr)
                cols[j].add(curr)
                block[i // 3][j // 3].add(curr)
        return True
#心得：每一个数字，属于三个不同的组织，它是rows, cols,也是blocks 
#block 是[[set(), set(), set()], [set(), set(), set()], [set(), set(), set()]]
#通过i和j来辨别在哪个block 