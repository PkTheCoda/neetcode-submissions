class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        absolute_max = 0
        local_max = 0
        visited = set()

        def dfs(row, col):
            print("dfs'ed")
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or (row, col) in visited or grid[row][col] == 0:
                return
            
            visited.add((row, col))
            nonlocal local_max
            local_max += 1
            print(local_max)

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                
                if (row, col) not in visited and grid[row][col] == 1:
                    dfs(row, col)
                    absolute_max = max(absolute_max, local_max)
                    local_max = 0
        
        return absolute_max