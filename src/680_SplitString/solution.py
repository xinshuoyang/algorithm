#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180326
#
################################################################################

class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        if len(s) == 0:
            return [[]]

        if len(s) == 1:
            return [[s[0]]]

        res = []
        self.helper([], s, res)
        return res

    def helper(self, prev, s, res):
        if len(s) == 1:
            res.append(prev + [s])
        elif len(s) == 2:
            res.append(prev + [s])
            res.append(prev + [s[0]] + [s[1]])
        else:
            self.helper(prev + [s[0]], s[1:], res)
            self.helper(prev + [s[:2]], s[2:], res)

if __name__ == '__main__':
    sol = Solution()
    print sol.splitString("1234")
