#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180322
#
################################################################################

class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here
        

        while b != 0:
            itmp = a ^ b

            b = (a & b) << 1

            a = itmp

            if a > 2147483647 or a < -2147483648:
                return 0
            
        return a


if __name__ == '__main__':
    sol = Solution()

    print sol.aplusb(1, -1)

