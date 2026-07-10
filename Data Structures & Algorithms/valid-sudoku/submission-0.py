class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x == ".":
                    continue
                k = ( i // 3) * 3 + ( j // 3)
                if x in rows[i] or x in cols[j] or x in boxes[k]:
                    return False
                rows[i].add(x)
                cols[j].add(x)
                boxes[k].add(x)
        return True
