from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[row])):

                if grid[row][col] == 0:
                    q.append((row, col, 0))
        
        while q:
            row, col, index = q.popleft()
            if (row, col) not in visited:
                visited.add((row, col))
            
            if grid[row][col] == 2147483647:
                grid[row][col] = index
            
            for rc, cc in directions:
                nr, nc = row + rc, col + cc

                if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[nr]) and (nr, nc) not in visited and grid[nr][nc] == 2147483647:
                    q.append((nr, nc, index + 1))
