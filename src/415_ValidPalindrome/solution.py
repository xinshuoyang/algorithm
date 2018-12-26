#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20181225
#
################################################################################

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # remove spaces and punctuation
        s = s.lower()
        dd = "abcdefghijklmnopqrstuvwxyz0123456789"
        ns = ""
        for i in range(len(s)):
            if s[i] in dd:
                ns += s[i]
                
        # check palindrome
        i = 0
        j = len(ns)-1
        
        while i <= j:
            if ns[i] != ns[j]:
                return False
            i += 1
            j -= 1
        return True

if __name__ == "__main__":
    ss = Solution()
    print ss.isPalindrome("race a car")
