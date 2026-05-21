class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new_nums = sorted(nums)
        res = []

        for i in range(len(new_nums)):
            fixed = 0 - new_nums[i]

            p1 = 0
            p2 = len(new_nums) - 1

            while p1 < p2:
                if new_nums[p1] + new_nums[p2] == fixed and p1 != i and p2 != i:
                    res.append([new_nums[i], new_nums[p1], new_nums[p2]])
                    p2 -= 1
                    p1 += 1
                elif new_nums[p1] + new_nums[p2] > fixed:
                    p2 -= 1
                else:
                    p1 += 1
        
        checked = {}
        cleaned = []
        for sol in res:
            if tuple(sorted(sol)) in checked:
                continue
            else:
                checked[tuple(sorted(sol))] = True
    
        
        for item in checked:
            cleaned.append(item)



        return cleaned

