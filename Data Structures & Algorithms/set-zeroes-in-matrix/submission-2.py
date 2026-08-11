class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # brute force
        rows = set()
        cols = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)
        
        for row in rows:
            matrix[row] = [0] * len(matrix[0])
        
        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0
                

                