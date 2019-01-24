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
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackIV(self, nums, target):
        # write your code here

        if target <= 0:
            return 0
        if not nums:
            return 0
        m = target
        n = len(nums)

        dp = [[0]*(m+1) for i in range(n)]

        for i in range(1,m+1):
            if i%nums[0] == 0:
                dp[0][i] = 1

        for i in range(1,n):
            for j in range(1,m+1):
                dp[i][j] = dp[i-1][j]
                for k in range(j,nums[i]-1,-nums[i]):
                    dp[i][j] += dp[i-1][k-nums[i]]
                if j%nums[i] == 0:
                    dp[i][j] += 1
        return dp[-1][-1]

if __name__ == "__main__":
    obj = Solution()
    print(obj.backPackIV([1,2,4], 8))
