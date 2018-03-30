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
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        if len(nums) == 1:
            return nums

        if len(nums) == 2:
            return [nums[1], nums[0]]

        #   whether it is the last permutation
        ifl = True
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                ifl = False
                break

        if ifl:
            return sorted(nums)

        ifl = False
        
        nmax = nums[-1]
        
        for i in range(len(nums) - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if nums[j] < nmax:

                    #   find the position of the smallest number > nums[j]
                    dmin = sys.maxint
                    for k in range(j + 1, len(nums)):
                        if nums[k] - nums[j] > 0 and dmin > nums[k]:
                            dmin = nums[k]
                            imin = k

                    # swap nums[j] and nums[imin]
                    temp = nums[j]
                    nums[j] = nums[imin]
                    nums[imin] = temp

                    start = j

                    ifl = True

                    break
                else:
                    if nmax < nums[j]:
                        nmax = nums[j]

            if ifl:
                break
        
        nums[start + 1:] = sorted(nums[start + 1:])
        
        return nums

if __name__ == '__main__':
    sol = Solution()
    print sol.nextPermutation([1,2,3,4,5,6,7,8,9,10,11,11,11,23,4,5,6,7,100,99,98,97,96,95,94,93,92,91,5])
