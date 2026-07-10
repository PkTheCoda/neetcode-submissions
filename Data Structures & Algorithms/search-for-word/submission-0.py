class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        solution = False

        def dfs(index, seen, row, col):
            if index > len(word) - 1 or board[row][col] != word[index]:
                return
            
            if index == len(word) - 1:
                nonlocal solution
                solution = True
                return
            
            # down 
            if row + 1 < len(board) and (row+1, col) not in seen:
                seen.add((row, col))
                dfs(index + 1, seen, row + 1, col)
                seen.discard((row, col))
            
            # up
            if row - 1 >= 0 and (row-1, col) not in seen:
                seen.add(((row, col)))
                dfs(index + 1, seen, row - 1, col)
                seen.discard((row, col))
            
            # left
            if col - 1 >= 0 and (row, col - 1) not in seen:
                seen.add(((row, col)))
                dfs(index + 1, seen, row, col - 1)
                seen.discard((row, col))
            
            # right
            if col + 1 < len(board[0]) and (row, col + 1) not in seen:
                seen.add(((row, col)))
                dfs(index + 1, seen, row, col + 1)
                seen.discard((row, col))

        
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(0, set(), row, col)
                
        
        return solution