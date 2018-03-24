#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180323
#
################################################################################

class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, s):
        # write your code here
        
        if len(s) <= 1:
            return [s]

        res = []
        self.helper(res, '', sorted(s))
        return res
        
    def helper(self, res, s, letters):
        
        if len(letters) == 1:
            res += [s + letters[0]]
        else:
            used = []

            for i in range(len(letters)):
                if letters[i] not in used:
                    self.helper(res, s + letters[i], letters[:i]+letters[i+1:])
                    used.append(letters[i])

if __name__ == '__main__':
    sol = Solution()
    print sol.stringPermutation2("cba")
