class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        absolute_max = 0
        visited = set()

        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or (row, col) in visited or grid[row][col] == 0:
                return 0
            
            visited.add((row, col))

            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                
                if (row, col) not in visited and grid[row][col] == 1:
                    absolute_max = max(absolute_max, dfs(row, col))
        
        return absolute_max