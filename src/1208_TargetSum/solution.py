#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20190115
#
################################################################################

class Solution:
    """
    @param nums: the given array
    @param s: the given target
    @return: the number of ways to assign symbols to make sum of integers equal to target S
    """
    def findTargetSumWays(self, nums, s):
        # Write your code here
        curr = 0
        return self.helper(nums,0,len(nums),curr,s)

    def helper(self,nums,i,n,curr,s):
        if i == n-1:
            r = 0
            if curr+nums[i] == s:
                r += 1
            if curr-nums[i] == s:
                r += 1
            return r
        elif i < n:
            return self.helper(nums,i+1,n,curr+nums[i],s)+self.helper(nums,i+1,n,curr-nums[i],s)

if __name__ == "__main__":
    obj = Solution()
    print(obj.findTargetSumWays([1,1,1,1,1], 3))
