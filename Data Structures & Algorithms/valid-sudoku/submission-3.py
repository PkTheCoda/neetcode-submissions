class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = defaultdict(set)
        col_hash = defaultdict(set)
        square_hash = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):

                if board[row][col] == ".":
                    continue
                

                if (board[row][col] in row_hash[row] or 
                    board[row][col] in col_hash[col] or 
                    board[row][col] in square_hash[(row // 3, col // 3)]):
                    return False

                row_hash[row].add(board[row][col])
                col_hash[col].add(board[row][col]) 
                square_hash[(row // 3, col // 3)].add(board[row][col])
        
        
        return True


