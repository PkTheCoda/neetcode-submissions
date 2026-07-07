class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(path, index):
            if sum(path) == target:
                res.append(list(path))
            
            if sum(path) > target: # input nums can only be positive, so return early
                return
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(path, i)
                path.pop()
                
        dfs([], 0)

        return res        