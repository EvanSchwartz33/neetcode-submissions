class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        inrow = {i: [] for i in range(9)}
        incolumn = {i: [] for i in range(9)}
        inbox = {i: {j: [] for j in range (3)} for i in range(3)}
        for i in range (0,9):
            for j in range (0,9):
                num = board[i][j]
                if num == ".":
                    continue
                if num in inrow[i]:
                    return False
                else:
                    inrow[i].append(num)
                if num in incolumn[j]:
                    return False
                else:
                    incolumn[j].append(num)
                if num in inbox[i//3][j//3]:
                    return False
                else:
                    inbox[i//3][j//3].append(num)

        return True
