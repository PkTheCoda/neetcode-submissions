class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # aab

        # dfs(path, index, combined_len)
        # dfs(["a"], 1, 1)

        res = []

        def dfs(path, index, combined_len):
            if combined_len == len(s):
                res.append(list(path))
                return
            
            for i in range(index, len(s)):
                to_append = s[index:i+1]
                is_palindrome = (to_append == to_append[::-1])
                
                if is_palindrome:
                    path.append(to_append)
                    dfs(path, i + 1, combined_len + len(to_append))
                    path.pop()
            
        
        dfs([], 0, 0)
        return res