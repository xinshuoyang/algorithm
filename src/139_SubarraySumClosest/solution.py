#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180303
#
################################################################################
import sys
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySumClosest(self, nums):
        
        # construct prefix sum array
        class prefix:
            def __init__(self, sums, index):
                self.sums, self.index = sums, index

            def __cmp__(self, other):
                return cmp(self.sums, other.sums)

        if len(nums) == 1:
            return 0, 0

        pp = [prefix(nums[0], 0)]

        for i in xrange(1, len(nums)):
            pp.append(prefix(pp[-1].sums + nums[i], i))

        # sort prefix array based on sums
        qq = sorted(pp)

        # find the smallest difference
        diff = sys.maxint
        for i in xrange(len(qq) - 1):
            if diff > abs(qq[i].sums - qq[i + 1].sums):
                diff = abs(qq[i].sums - qq[i + 1].sums)
                first, last = qq[i].index, qq[i + 1].index
        return min(first, last) + 1, max(first, last)

if __name__ == '__main__':
    s = Solution()
    print s.subarraySumClosest([-3,1,1,-3,5])
