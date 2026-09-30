class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        output = []
        ptr = 0

        while ptr < len(intervals):
            current_min = intervals[ptr][0]
            current_max = intervals[ptr][1]

            while ptr < len(intervals) and intervals[ptr][0] <= current_max:
                current_max = max(current_max, intervals[ptr][1])
                current_min = min(current_min, intervals[ptr][0])
                ptr += 1
            
            output.append([current_min, current_max])

        
        return output