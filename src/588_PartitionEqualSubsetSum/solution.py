#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20190123
#
################################################################################

class Solution:
    """
    @param nums: a non-empty array only positive integers
    @return: true if can partition or false
    """
    def canPartition(self, nums):
        # write your code here
        if not nums or len(nums) <= 1:
            return False
        ss = sum(nums)
        if ss%2 != 0:
            return False

        m = ss//2
        n = len(nums)

        dp = [[False]*(m+1) for i in range(n)]

        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True

        for i in range(1,n):
            for j in range(1,m+1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i]:
                    dp[i][j] = dp[i-1][j-nums[i]]
            if dp[i][-1]:
                return True
        return False

if __name__ == "__main__":
    obj = Solution()
    print(obj.canPartition([1, 5, 11, 5]))
    
