#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20190107
#
##################################################
class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        if not nums:
            return 0

        leftsums = [nums[0]]
        if leftsums[0] == k:
            res = 1
        else:
            res = 0

        for i in range(1,len(nums)):
            leftsums.append(leftsums[-1]+nums[i])
            if leftsums[-1] == k and res < i+1:
                res = i+1

        hh = {}
        for i in range(len(nums)-1,-1,-1):
            if leftsums[i]+k in hh:
                res = max(res,hh[leftsums[i]+k]-i)
            if leftsums[i] not in hh:
                hh[leftsums[i]] = i
        return res

if __name__ == "__main__":
    obj = Solution()
    print(obj.maxSubArrayLen([-2,-1,2,1],1))
