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
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        # write your code here
        import math
        
        if amount <= 0:
            return 0
        if not coins:
            return -1
        
        dp = [0]+[math.inf]*amount
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i],dp[i-coins[j]]+1)
        if dp[-1] == math.inf:
            return -1
        else:
            return dp[-1]
        
if __name__ == "__main__":
    obj = Solution()
    obj.coinChange([1,2,4],32000)
