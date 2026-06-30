"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        #sort by starting time
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        mx_overlaps = 0
        current = 0
        s = e = 0

        while s < len(starts) and e < len(ends):
            if starts[s] < ends[e]:
                current += 1
                
                mx_overlaps = max(mx_overlaps, current)
                s += 1

            
            else:
                current -= 1
                e += 1

        return mx_overlaps




