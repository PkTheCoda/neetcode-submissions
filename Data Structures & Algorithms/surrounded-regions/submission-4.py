from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q = deque()

        for row in range(len(board)):
            for col in range(len(board[0])):
                if row == 0 or col == 0 or row == len(board) -1 or col == len(board[0]) - 1:
                    if board[row][col] == "O":
                        board[row][col] = "safe"
                        q.append((row, col))
        
        while q:
            row, col = q.popleft()

            for rc, cc in directions:
                nr = row + rc
                nc = col + cc

                if nr >= 0 and nc >= 0 and nr < len(board) and nc < len(board[0]) and board[nr][nc] == "O":
                    board[nr][nc] = "safe"
                    q.append((nr, nc))
        

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "safe":
                    board[row][col] = "O"