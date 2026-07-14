from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            
            grid[row][col] = "0"

            for cr, cc in directions:
                nr, nc = row + cr, col + cc

                if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[nr]) and grid[nr][nc] == "1":
                    dfs(nr, nc)
            


        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    count += 1

                    dfs(row, col)
        
        return count
        