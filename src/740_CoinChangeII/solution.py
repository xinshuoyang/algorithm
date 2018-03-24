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
        
        if amount == 0:
            return 0

        dp = []
        
        for i in range(len(amount)):
            


if __name__ == '__main__':
    amount = 123
    coins = [2,3,8]
    s = Solution()
    print s.change(amount, coins)
    
