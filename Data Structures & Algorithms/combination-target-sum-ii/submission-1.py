class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)

        def dfs(path, index, total):
            if total > target:
                return
            
            if total == target:
                res.append(list(path))
            
            for i in range(index, len(candidates)):
                if i != index and candidates[i] == candidates[i - 1]:
                    continue
                
                if total + candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(path, i + 1, total + candidates[i])
                path.pop()

        dfs([], 0, 0)

        return res