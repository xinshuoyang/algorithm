#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20190104
#
################################################################################

class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        # write your code here
        d = {ll:0 for ll in s}
        for ll in s:
            if d[ll] is 0:
                d[ll] = 1
            else:
                d[ll] = 0
        num = 0
        for ll in d:
            num += d[ll]

        if num > 1:
            return False
        else:
            return True
if __name__ == "__main__":
    obj = Solution()
    print(obj.canPermutePalindrome('code'))
