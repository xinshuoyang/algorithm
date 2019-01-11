#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20190110
#
################################################################################

class Solution:
    """
    @param nums: the given sequence
    @return: the length of the longest subsequence that is a wiggle sequence
    """
    def wiggleMaxLength(self, nums):
        # Write your code here
        if len(nums) <= 2:
            return len(nums)

        j = 0
        while nums[j+1]-nums[j] == 0 and j+1 < len(nums):
            j += 1
        diff1 = nums[j+1]-nums[j]
        res = 1

        for i in range(2,len(nums)):
            diff2 = nums[i]-nums[i-1]
            if diff1*diff2 < 0:
                res += 1
                diff1 = diff2
            else:
                diff1 += diff2
            print(diff1,res)
        return res+1
if __name__ == "__main__":
    obj = Solution()
    print(obj.wiggleMaxLength([3,3,3,2,5]))
