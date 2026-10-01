class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            grid[row][col] = "0"
            visited.add((row, col))

            for row_dir, col_dir in directions:
                nr, nc = row + row_dir, col + col_dir

                if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]) and (nr,nc) not in visited and grid[nr][nc] == "1":
                    dfs(nr, nc)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    count += 1

                    dfs(i, j)
        
        return count
                