#!/usr/bin/python

##################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180327
#
##################################################


class Solution:
    """
    @param num: a positive integer
    @return: if num is a perfect square else False
    """
    def isPerfectSquare(self, num):
        if num == 1:
            return True

        first = 1
        last = num

        while last - first > 1:
            mid = first + (last - first) / 2

            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                first = mid
            else:
                last = mid

        
        if first ** 2 == num or last ** 2 == num:
            return True
        else:
            return False


#    def isPerfectSquare(self, num):
#        # write your code here
#
#        sqrtnum = int(self.newton(num))
#        if sqrtnum ** 2 == num or (sqrtnum + 1) ** 2 == num:
#            return True
#        else:
#            return False
#
#    def newton(self, n):
#        
#        x0 = 10.0
#        err = 1
#
#        while err > 0.01:
#            x1 = x0 - (x0 ** 2.0 - n) / x0 / 2.0
#            err = abs(x1 - x0)
#            x0 = x1
#
#        return x0

if __name__ == '__main__':
    sol = Solution()
    print sol.isPerfectSquare(2532)
