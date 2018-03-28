#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180327
#
################################################################################
class Solution:
    """
    @param a: a positive integer
    @return: the smallest positive integer whose multiplication of each digit equals to a
    """
    def smallestFactorization(self, a):

        # find a factorization of a with factors less than 10
        factors = []
        
        while a >= 10:
            ifl = False
            for i in range(9, 2, -1):
                if a % i == 0:
                    factors.append(i)
                    a = a / i
                    ifl = True
                    break
            if not ifl:
                return 0
        factors.append(a)
        digits = sorted(factors)
        res = 0

        for i in range(len(digits)):
            res += 10 ** i * digits[len(digits) - i - 1]
            
        if res > 2 ** 31 - 1:
            return 0
        else:
            return res

if __name__ == '__main__':
    sol = Solution()
    print sol.smallestFactorization(18000000)                                                                                                                                                                                                                                                  

            
