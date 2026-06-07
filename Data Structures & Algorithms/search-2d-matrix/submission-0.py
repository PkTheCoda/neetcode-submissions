class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute force
        for array in matrix:
            for item in array:
                if item == target:
                    return True
        
        return False
        