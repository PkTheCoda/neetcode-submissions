class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        num_len = len(nums)

        def dfs(path, used):
            if len(path) > num_len:
                return
            
            if len(path) == num_len:
                res.append(list(path))

            for num in nums:
                if num not in used:
                    path.append(num)
                    used.add(num)
                    dfs(path, used)
                    path.pop()
                    used.remove(num)
        
        dfs([], set())

        return res