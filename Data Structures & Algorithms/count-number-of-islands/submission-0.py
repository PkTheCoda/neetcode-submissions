from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or (row, col) in visited or grid[row][col] == "0":
                return
            
            grid[row][col] == "0"
            visited.add((row, col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            


        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if (row, col) not in visited and grid[row][col] == "1":
                    count += 1

                    dfs(row, col)
        
        return count
        