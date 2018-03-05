#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180304
#
################################################################################
import math
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        
        if n <= 1:
            return (a ** n) % b

        maxpow = int(math.log(n, 2))

        reminder = [a % b]
        for p in xrange(maxpow):
            reminder.append((reminder[-1] ** 2) % b)

        n -= 2 ** maxpow
        res = reminder[-1]

        for p in xrange(maxpow - 1, -1, -1):
            if n >= 2 ** p:
                res = (res * reminder[p]) % b
                n -= 2 ** p

        return res 
            
if __name__ == '__main__':

    sol = Solution()
    print sol.fastPower(100, 1000, 1000)

        
