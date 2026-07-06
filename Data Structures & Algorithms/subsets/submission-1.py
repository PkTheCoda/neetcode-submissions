class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path, nums):

            res.append(list(path))
            
            for i in range(len(nums)):
                path.append(nums[i])
                dfs(path, nums[i + 1:])
                path.pop()
        
        dfs([], nums)

        return res
