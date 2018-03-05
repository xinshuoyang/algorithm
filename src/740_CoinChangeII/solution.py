#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20171211
#
################################################################################

class Solution:
    """
    @param amount: a total amount of money amount
    @param coins: the denomination of each coin
    @return: the number of combinations that make up the amount
    """
    def change(self, amount, coins):
        # write your code here
        counts = [0]
        self.helper(amount, coins, counts)

        return counts[0]
    
    def helper(self, amount, coins, counts):
        if amount > 0:
            for i in range(len(coins)):
                if coins[i] == amount:
                    counts[0] += 1
                elif coins[i] < amount:
                    self.helper(amount - coins[i], coins[i:], counts)

if __name__ == '__main__':
    amount = 8
    coins = [2, 3, 8]
    
    s = Solution()
    print s.change(amount, coins)
    
