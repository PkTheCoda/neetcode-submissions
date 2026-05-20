class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = {}
        col_hash = {}
        square_hash = {}

        for row in range(len(board)):
            for col in range(len(board)):

                if board[row][col] == ".":
                    continue
                

                curr = board[row][col]

                if row in row_hash:
                    if curr in row_hash[row]:
                        return False
                    else:
                        row_hash[row].add(curr)
                else:
                    row_hash[row] = {curr}

                if col in col_hash:
                    if curr in col_hash[col]:
                        return False
                    else:
                        col_hash[col].add(curr)
                else:
                    col_hash[col] = {curr}
                
                curr_square = (row // 3) * 3 + (col // 3) 
                if curr_square in square_hash:
                    if curr in square_hash[curr_square]:
                        return False
                    else:
                        square_hash[curr_square].add(curr)
                else:
                    square_hash[curr_square] = {curr}
        
        
        return True


