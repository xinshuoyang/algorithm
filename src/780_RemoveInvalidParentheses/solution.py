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
import sys
class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        # Write your code here
        nl = 0
        nr = 0
        nrm = 0

        prev = ''
        res = [sys.maxint]

        self.helper(nl, nr, nrm, prev, s, res)
        return res

    def helper(self, nl, nr, nrm, prev, s, res):
        print 'prev', prev
        print 's', s
        if len(s) == 0:
            if nl == nr and nrm <= res[0]:
                if nrm < res[0]:
                    res[0] = nrm
                res.append(prev)
        else:
            if s[0] == '(':
                self.helper(nl + 1, nr, nrm, prev + s[0], s[1:], res)

            elif s[0] == ')':
                if nl > nr:
                    self.helper(nl, nr + 1, nrm, prev + s[0], s[1:], res)
                
                if nrm + 1 <= res[0]:
                    self.helper(nl, nr, nrm + 1, prev, s[1:], res)
            else:
                self.helper(nl, nr, nrm, prev + s[0], s[1:], res)

if __name__ == '__main__':
    sol = Solution()
    print sol.removeInvalidParentheses("()())()")
