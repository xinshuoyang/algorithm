#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20190107
#
##################################################
class Solution:
    """
    @param s: a string represent DNA sequences
    @return: all the 10-letter-long sequences 
    """
    def findRepeatedDna(self, s):
        # write your code here
        if len(s) < 10:
            return []
        
        hh = {}
        for i in range(len(s)-9):
            if s[i:i+10] in hh:
                hh[s[i:i+10]] += 1
            else:
                hh[s[i:i+10]] = 1
            #print(hh)
                
        res = []
        for i in hh:
            if hh[i] >= 2:
                res.append(i)
        return res
if __name__ == "__main__":
    obj = Solution()
    print(obj.findRepeatedDna("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
