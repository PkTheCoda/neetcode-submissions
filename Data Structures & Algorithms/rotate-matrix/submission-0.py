class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # (0,0) (0,1) (0,2)
        # (0,2) (1,2) (2,2)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(len(matrix)):
            matrix[i].reverse()
        

        