#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180330
#
################################################################################
import sys
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """
    def previousPermuation(self, nums):
        # write your code here

        if len(nums) == 1:
            return nums

        if len(nums) == 2:
            return [nums[1], nums[0]]

        ifl = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                ifl = False

        if ifl:
            return sorted(nums, reverse=True)

        ifl = False
        
        nmin = nums[-1]
        
        for i in range(len(nums) - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if nums[j] > nmin:

                    #   find the position of the greatest number < nums[j]
                    dmax = - sys.maxint - 1
                    for k in range(j + 1, len(nums)):
                        if nums[j] - nums[k] > 0 and dmax < nums[k]:
                            dmax = nums[k]
                            imax = k

                    # swap nums[j] and nums[imin]
                    temp = nums[j]
                    nums[j] = nums[imax]
                    nums[imax] = temp

                    start = j

                    ifl = True

                    break
                else:
                    if nmin > nums[j]:
                        nmin = nums[j]

            if ifl:
                break
        
        nums[start + 1:] = sorted(nums[start + 1:], reverse=True)
        
        return nums

if __name__ == '__main__':
    sol = Solution()
    print sol.previousPermuation([1,3,2,3])
