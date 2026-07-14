from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def bfs(row, col):
            # something
            q = deque()
            visited = set()

            q.append((row, col, 0))

            while q:
                row, col, level = q.popleft()
                visited.add((row, col))

                if grid[row][col] == 0:
                    return level

                for rchange, cchange in directions:
                    r_new = row + rchange
                    c_new = col + cchange

                    if r_new >= 0 and c_new >= 0 and r_new < len(grid) and c_new < len(grid[r_new]) and (r_new, c_new) not in visited and grid[r_new][c_new] != -1:
                        q.append((r_new, c_new, level + 1))

            # cant find chest, so keep infinity
            return 2147483647
        

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2147483647:
                    grid[row][col] = bfs(row, col)
        