class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        out = [intervals[0]]

        ptr = 1
        while ptr < len(intervals):
            # do we extend out's latest element or just add ours
            if intervals[ptr][0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], intervals[ptr][1])
            else:
                out.append(intervals[ptr])
            
            ptr += 1
        
        return out