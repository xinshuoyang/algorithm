#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180326
#
################################################################################

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here

        if len(prices) <= 1:
            return 0

        if len(prices) == 2:
            return max(prices[1] - prices[0], 0)
        
        if len(prices) == 3:
            return max([0, prices[1] - prices[0], prices[2] - prices[0], prices[2] - prices[1]])
 
        # forward
        p1 = [0, max(prices[1] - prices[0], 0)]
        l1 = min(prices[:2])
        
        for i in range(2, len(prices)):
            if prices[i] > l1:
                p1.append(max(prices[i] - l1, p1[-1]))
            else:
                l1 = prices[i]
                p1.append(p1[-1])

        # backward
        if prices[-2] < prices[-1]:
            p2 = [0, prices[-1] - prices[-2]]
            h2 = prices[-1]
        else:
            p2 = [0, 0]
            h2 = prices[-2]
        
        for i in range(3, len(prices) + 1):
            if prices[-i] < h2:
                p2.append(max(p2[-1], h2 - prices[-i]))
            else:
                h2 = prices[-i]
                p2.append(p2[-1])

        ptot = 0 

        for i in range(len(prices)):
            if ptot < p1[i] + p2[len(prices) - i - 1]:
                ptot = p1[i] + p2[len(prices) - i - 1]
        
        return ptot

if __name__ == '__main__':
    sol = Solution()
    print sol.maxProfit([5,7,2,7,3])
