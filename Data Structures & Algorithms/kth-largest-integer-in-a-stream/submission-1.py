class KthLargest:
    # brute force
    def __init__(self, k: int, nums: List[int]):
        self.index = k
        self.nums = sorted(nums)
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums = sorted(self.nums)
        return self.nums[-self.index]
        
