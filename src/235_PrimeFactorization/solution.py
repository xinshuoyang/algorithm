#!/usr/bin/python

##################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180328
#
##################################################
import math
class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        # write your code here

        if num == 1:
            return [1]

        if num == 2:
            return [2]

        factors = []

        while True:
            t1, t2 = self.factor(num)
            
            if (t1, t2) == (0, 0):
                factors.append(num)
                return factors
            else:
                factors.append(t1)
                num = t2

    def factor(self, num):
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return i, num / i
        return 0, 0

if __name__ == '__main__':
    sol = Solution()
    print sol.primeFactorization(6231)
