class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        i = 0
        count = 0
        while i < len(intervals):
            curr_interval = intervals[i]
            i += 1

            while i < len(intervals) and intervals[i][0] < curr_interval[1]:
                i += 1
                count += 1



        return count