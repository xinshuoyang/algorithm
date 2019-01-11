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
    @param prices: a list of integers
    @return: return a integer
    """
    def maxProfit(self, prices):
        # write your code here
        if len(prices) <= 1:
            return 0
        if len(prices) == 2:
            return max(0,prices[1]-prices[0])
        if len(prices) == 3:
            return max(0,prices[1]-prices[0],prices[2]-prices[1],prices[2]-prices[0])
            
        dp = [0,prices[1]-prices[0],max(prices[2]-prices[1],prices[2]-prices[0])]
        for i in range(3,len(prices)):
            dp.append(max(prices[i]-prices[0],prices[i]-prices[1],prices[i]-prices[2]))
    
            for j in range(1,i-2):
                dp[-1] = max(dp[-1],dp[j]+max([dp[i]-dp[k] for k in range(j+2,i)]))

        print(dp)
        return max(0,max(dp))

if __name__ == "__main__":
    obj = Solution()
    obj.maxProfit([1,2,3,0,2,53,2,34,6,3,6,4,8,9,5])
