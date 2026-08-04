class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Rows
        for r in range(9):
            row = [board[r][c] for c in range(9) if board[r][c] != '.']
            if len(row) != len(set(row)):
                return False

        # Columns
        for c in range(9):
            col = [board[r][c] for r in range(9) if board[r][c] != '.']
            if len(col) != len(set(col)):
                return False

        # Sub-grids
        def in_range(a, lo, hi):
            return lo <= a <= hi

        def box_index(r, c):
            match (r, c):
                case (r, c) if in_range(r, 0, 2) and in_range(c, 0, 2): return 0
                case (r, c) if in_range(r, 0, 2) and in_range(c, 3, 5): return 1
                case (r, c) if in_range(r, 0, 2) and in_range(c, 6, 8): return 2
                case (r, c) if in_range(r, 3, 5) and in_range(c, 0, 2): return 3
                case (r, c) if in_range(r, 3, 5) and in_range(c, 3, 5): return 4
                case (r, c) if in_range(r, 3, 5) and in_range(c, 6, 8): return 5
                case (r, c) if in_range(r, 6, 8) and in_range(c, 0, 2): return 6
                case (r, c) if in_range(r, 6, 8) and in_range(c, 3, 5): return 7
                case (r, c) if in_range(r, 6, 8) and in_range(c, 6, 8): return 8
                case _:
                    raise ValueError(f"no box for ({r},{c})")

        boxes = [[] for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    boxes[box_index(r, c)].append(board[r][c])

        for box in boxes:
            if len(box) != len(set(box)):
                return False

        return True