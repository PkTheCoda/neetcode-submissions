class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        first_row_zero = False
        first_col_zero = False

        for num in matrix[0]:
            if num == 0:
                first_row_zero = True
        
        for l in range(len(matrix)):
            if matrix[l][0] == 0:
                first_col_zero = True

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        # replace all rows
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(len(matrix)):
                    matrix[j][i] = 0
        
        # replace all cols
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                matrix[i] = [0] * len(matrix[0])
        
        if first_row_zero:
            matrix[0] = [0] * len(matrix[0])

        if first_col_zero:
            for k in range(len(matrix)):
                matrix[k][0] = 0
        
        