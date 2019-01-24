#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20190120
#
################################################################################
"""
Definition of Interval.
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        if not intervals:
            return 0
        sint = sorted(intervals, key = lambda x:x.start)
        rooms = [sint[0]]
        for i in range(1,len(sint)):
            conflict = True
            for j in range(len(rooms)):
                if sint[i].start >= rooms[j].end:
                    rooms[j] = sint[i]
                    conflict = False
                    break
            if conflict:
                rooms.append(sint[i])
            print(rooms)
        return len(rooms)

if __name__ == "__main__":
    obj = Solution()
    intervals = [Interval(0,30),Interval(5,10),Interval(15,20)]
    print(obj.minMeetingRooms(intervals))
