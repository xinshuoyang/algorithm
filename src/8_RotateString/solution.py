#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180303
#
################################################################################

class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        # write your code here
        if len(s) > 0:
            offset = offset % len(s)
            
        temp = (s + s)[len(s) - offset : 2 * len(s) - offset]

        for i in xrange(len(temp)):
            s[i] = temp[i]


if __name__ == '__main__':
    sol = Solution()
    s = 'abcdefg'
    sol.rotateString(s, 3)
    print s
