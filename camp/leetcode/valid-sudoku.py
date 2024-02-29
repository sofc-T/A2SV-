class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = set()
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    if (i, element) in res or (element, j) in res or (i // 3, j // 3, element) in res :
                        return False
                    res.add((i, element))
                    res.add((element, j))
                    res.add((i // 3, j // 3, element))
        return True