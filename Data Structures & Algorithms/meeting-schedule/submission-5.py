"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda i:i.start)
        for first in range(len(intervals)):
            for second in range(first + 1, len(intervals)):
                if intervals[second].start < intervals[first].end:
                    return False
        return True
