from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        elapsed = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    q.append((row, col, 0))
                    visited.add((row, col))
        
        while q:
            row, col, curr_time = q.popleft()

            elapsed = curr_time

            grid[row][col] = 2

            for rc, cc in directions:
                nr = row + rc
                nc = col + cc

                if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[nr]) and (nr, nc) not in visited and grid[nr][nc] == 1:
                    # this means in bound, unvisited fresh fruit
                    visited.add((nr, nc))
                    q.append((nr, nc, curr_time + 1))
        
        print(grid)
        print(elapsed)
        print(visited)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    return -1 # theres an unreachable fresh fruit hiding somewhere we can't reach
        
        return elapsed