"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda interval: interval.start)
        i = 0
        while i < len(intervals) - 1:
            curr_interval = intervals[i]
            i += 1
            if i < len(intervals) and intervals[i].start < curr_interval.end:
                return False
        
        return True