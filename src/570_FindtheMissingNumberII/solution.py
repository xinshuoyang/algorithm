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
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, s):
        decomp = []
        prev = []
        self.decompstring(prev, n, s, decomp)
        
        for dd in decomp:
            if len(dd) == n - 1:
                ll = sorted(dd)
                break
        
        for i in range(n - 1):
            if i + 1 != ll[i]:
                return i + 1

        return n
            
    def decompstring(self, prev, n, s, res):
        if len(s) == 1:
            if int(s[0]) not in prev and int(s[0]) <= n and int(s[0]) > 0:
                res.append(prev + [int(s[0])])
        elif len(s) == 2:
            if int(s[0]) > 0:
                if int(s) not in prev and int(s) <= n:
                    res.append(prev + [int(s)])

            if s[0] != s[1]:
                if int(s[0]) not in prev and int(s[0]) <= n  and int(s[0]) > 0\
                        and int(s[1]) not in prev and int(s[1]) <= n and int(s[1]) > 0:
                    res.append(prev + [int(s[0]), int(s[1])])
        else:
            if int(s[0]) not in prev and int(s[0]) <= n and int(s[0]) > 0:
                self.decompstring(prev + [int(s[0])], n, s[1:], res)
            if int(s[0]) > 0:
                if int(s[:2]) not in prev and int(s[:2]) <= n:
                    self.decompstring(prev + [int(s[:2])], n, s[2:], res)


        

if __name__ == '__main__':
    sol = Solution()
    print sol.findMissing2(28,"111097654281222131272625242321320191817161514")
