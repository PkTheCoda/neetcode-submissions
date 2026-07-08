class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        def dfs(path, index):
            if len(path) > len(nums):
                return
            
            res.append(list(path))

            for i in range(index, len(nums)):
                if i != index and nums[i] == nums[i - 1]:
                    continue
                
                path.append(nums[i])
                dfs(path, i + 1)
                path.pop()
                

        dfs([], 0)

        return res
