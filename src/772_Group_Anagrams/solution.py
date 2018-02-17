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

class Solution:
    """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
    """
    def groupAnagrams(self, strs):
        # write your code here

        dd = {}

        for ss in strs:
            tt = ''.join(sorted(ss))
           
            if dd.has_key(tt):
                dd[tt] += [ss]
            else:
                dd[tt] = [ss]
        res = []

        for kk in dd:
            res += [dd[kk]]

        
        return res


if __name__ == '__main__':
    s = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]

    print s.groupAnagrams(strs)
