#!/usr/bin/python

##################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180326
#
##################################################
import math
class Solution:
    """
    @param n: the number
    @return: the rank of the number
    """
    def kthPrime(self, n):
        # write your code here

        if n == 2:
            return 1
        if n == 3:
            return 2
        else:
            counts = 2
            for i in range(5, n, 2):
                if self.isPrime(i):
                    counts += 1

            return counts + 1
        

    def isPrime(self, n):
        for i in range(3, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print sol.kthPrime(11)
