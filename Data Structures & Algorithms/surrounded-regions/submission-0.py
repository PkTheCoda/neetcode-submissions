from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # loop thru every cell
        # if we hit an O
            # then run a bfs. add the 0 (and any adjacent 0's) to the queue
            # if we EVER hit out of bounds, that means an O is an edge and thus cant be surrounded
            # return empty array ([])
            # but if we get through the entire thing and map out all O's. it CAN be surrounded.
            # so return [visited] (all O's by row,col)
        # back in original loop, if "0" and if bfs returns an array, replace entire array with "X"

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
