#!/usr/bin/python

##################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180324
#
##################################################
class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """
    def gcd(self, a, b):
        # write your code here
        if a == 0:
            return b
        if b == 0:
            return a

        x = max(abs(a), abs(b))
        y = min(abs(a), abs(b))
        
        r = x % y

        while r != 0:
            x = y
            y = r
            r = x % y

        return y




if __name__ == '__main__':
    sol = Solution()
    print sol.gcd( - 1, 1)
