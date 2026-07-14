class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = []
        visited = set()
        count = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or (row, col) in visited or grid[row][col] == "0":
                return
            
            visited.add((row, col))

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    count += 1

                    dfs(row, col)
        
        return count