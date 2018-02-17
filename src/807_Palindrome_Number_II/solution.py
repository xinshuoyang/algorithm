#!/usr/bin/python

##################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180217
#
##################################################

import math
class Solution:
    """
    @param n: non-negative integer n.
    @return: return whether a binary representation of a non-negative integer n is a palindrome.
    """
    def isPalindrome(self, n):
        # Write your code here
        
        if n == 0:
            return True

        binary = []

        ppmax = int(math.log(n, 2))

        for pp in xrange(ppmax, -1, -1):

            dig = n / (2 ** pp)

            if dig == 1:
                n -= 2 ** pp

            binary += [dig]
        
        #   check palindrome
        for i in xrange(0, len(binary) / 2):
            if binary[i] != binary[-i-1]:
                return False

        return True

if __name__ == '__main__':

    s = Solution()
    print s.isPalindrome(0)
