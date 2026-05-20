class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        combinations = list(board)

        for x in range(len(board)):
            curr_col = []
            for y in range(len(board)):
                curr_col.append(board[y][x])

            combinations.append(curr_col)
        
        # now all rows & cols r added to combinations, now just squares

        # x and y r same
        coords = [[0,2], [3,5], [6,8]]


        for x in coords:
            for y in coords:

                # print(f"x {x}, y {y}")
                curr_square = []
                for x_loop in range(x[0], x[1] + 1):
                    for y_loop in range(y[0], y[1] + 1):
                        curr_square.append(board[x_loop][y_loop])
                
                combinations.append(curr_square)
        

        cleaned_combos = []
        for combo in combinations:
            cleaned = []
            for item in combo:
                if item in "0123456789":
                    cleaned.append(item)
            
            cleaned_combos.append(cleaned)
        
        print(cleaned_combos)
        
        for combo in cleaned_combos:
            if len(combo) != len(set(combo)):
                return False
        
        return True

                



        return True
        