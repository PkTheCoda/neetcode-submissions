class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp[r][c] = minimum path sum at cell (r,c)
        # dp bottom left is just bl + minimum(dp[left to bl], dp[up to bl])
            # bl = bottom left
        
        dp = [[300] * len(grid[0]) for i in range(len(grid))]

        dp[0][0] = grid[0][0]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                left_val = float('inf')
                up_val = float('inf')

                if row - 1 >= 0:
                    up_val = dp[row - 1][col]
                
                if col - 1 >= 0:
                    left_val = dp[row][col - 1]
                
                if (row, col) != (0,0):
                    dp[row][col] = min(left_val, up_val) + grid[row][col]

        return dp[len(grid) - 1][len(grid[0]) - 1]