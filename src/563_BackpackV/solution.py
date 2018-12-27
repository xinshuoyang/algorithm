#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20181226
#
################################################################################

class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        if not nums or target == 0:
            return 0
        nums = sorted(nums)
        dp = [[0]*(target+1) for i in range(len(nums)+1)]
        
        for i in range(1, target+1):
            if nums[0] == i:
                dp[1][i] = 1
            else:
                dp[1][i] = 0

        for i in range(1,len(nums)):
            for j in range(1, target+1):
                if nums[i] > j:
                    dp[i+1][j] = dp[i][j]
                elif nums[i] == j:
                    #if nums[i] == nums[i-1]:
                    #    dp[i+1][j] = dp[i][j]
                    #else:
                    dp[i+1][j] = dp[i][j]+1
                else:
                    dp[i+1][j] = dp[i][j]+dp[i][j-nums[i]]
        #print(dp)
        return dp[len(nums)][target]

if __name__ == "__main__":
    ss = Solution()
    print ss.backPackV([81,112,609,341,164,601,97,709,944,828,627,730,460,523,643,901,602,508,401,442,738,443,555,471,97,644,184,964,418,492,920,897,99,711,916,178,189,202,72,692,86,716,588,297,512,605,209,100,107,938,246,251,921,767,825,133,465,224,807,455,179,436,201,842,325,694,132,891,973,107,284,203,272,538,137,248,329,234,175,108,745,708,453,101,823,937,639,485,524,660,873,367,153,191,756,162,50,267,166,996,552,675,383,615,985,339,868,393,178,932],800000)
