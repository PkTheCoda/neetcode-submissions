class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        mapped = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(string, index):
            if index == len(digits):
                res.append(string)
                return
            

            for char in mapped[digits[index]]:
                dfs(string + char, index + 1)

        dfs("", 0)

        return res
        