from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) #key row
        columns = defaultdict(set) #key column
        sub_grid = defaultdict(set) #key (r//3, c//3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or board[r][c] in columns[c] 
                or board[r][c]  in sub_grid[(r//3, c//3)]): return False

                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                sub_grid[(r//3, c//3)].add(board[r][c])

        return True