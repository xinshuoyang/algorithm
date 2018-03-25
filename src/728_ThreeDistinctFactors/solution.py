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
import math

class Solution:
    """
    @param n: the given number
    @return: true if it has exactly three distinct factors, otherwise false
    """

    def isThreeDisctFactors(self, n):
        # write your code here
        
        sqrtn = int(math.sqrt(n))

        if n == sqrtn * sqrtn:
            if self.isPrime(sqrtn):
                return True

        return False 

    def isPrime(self, n):

        if n <= 11:
            if n in [2, 3, 5, 7, 11]:
                return True
            else:
                return False

        else:
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False

            return True

if __name__ == '__main__':

    sol = Solution()
    print sol.isThreeDisctFactors(169)
