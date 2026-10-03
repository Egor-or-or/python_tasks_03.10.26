class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        row = len(board)
        col = len(board[0])

        directions =  [(-1, -1), (-1, 0), (-1, 1),
                       (0, -1),            (0, 1),
                       (1, -1),  (1, 0),  (1, 1)]
        for r in range(row):
            for c in range(col):
                live_neighbours = 0

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < row and 0 <= nc < col:
                        if board[nr][nc] == 1 or board[nr][nc] == 2:
                            live_neighbours += 1
                if board[r][c] == 1:
                    if live_neighbours < 2 or live_neighbours > 3:
                        board[r][c] = 2
                else:
                    if live_neighbours == 3:
                        board[r][c] = 3
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1
