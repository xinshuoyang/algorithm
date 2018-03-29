#!/usr/bin/python

##################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180328
#
##################################################

class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        # Write your code here
        
        m = len(words)
        n = max([len(s) for s in words])

        l = max(m, n)

        for i in range(m):
            if len(words[i]) < l:
                words[i] += ' ' * (l - len(words[i]))

        for i in range(l):
            row = words[i]
            col = ''
            for j in range(m):
                col += words[j][i]

            if row != col:
                return False

        return True

if __name__ == '__main__':
    sol = Solution()
    print sol.validWordSquare([
  "ball",
  "area",
  "read",
  "lady"
])
