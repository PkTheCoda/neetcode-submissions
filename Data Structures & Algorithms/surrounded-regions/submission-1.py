from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(row, col):
            visited = []
            q = deque()
            q.append((row, col))
            visited.append((row, col))

            while q:
                row, col = q.popleft()

                for rc, cc in directions:
                    nr = row + rc
                    nc = col + cc

                    if nr < 0 or nc < 0 or nr >= len(board) or nc >= len(board[0]):
                        return [] # the "O" we found was an edge piece. part can't be surrounded
                    elif (nr, nc) not in visited and board[nr][nc] == "O":
                        visited.append((nr, nc))
                        q.append((nr, nc))
            
            return visited
        
        for row in range(len(board)):
            for col in range(len(board[0])):

                if board[row][col] == "O":
                    returned = bfs(row, col)
                    if returned:
                        for rr, rc in returned:
                            board[rr][rc] = "X"
