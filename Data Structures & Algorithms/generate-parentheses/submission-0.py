class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # for 2:
        # ()() (()) 
        res = []

        def dfs(string, open_count, close_count):
            if len(string) > (n * 2):
                return
            
            if len(string) == (n * 2):
                res.append(string[:])
                
            
            if open_count < n:
                string += "("
                open_count += 1
                dfs(string, open_count, close_count)
                string = string[:-1]
                open_count -= 1
            
            if close_count < open_count:
                string += ")"
                close_count += 1
                dfs(string, open_count, close_count)
                string = string[:-1]
                close_count -= 1

            

        
        dfs("", 0, 0)
        return res
