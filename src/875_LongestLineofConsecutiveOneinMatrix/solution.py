#!/usr/bin/python

##################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180331
#
##################################################

class Solution:
    """
    @param M: the 01 matrix
    @return: the longest line of consecutive one in the matrix
    """
    def longestLine(self, M):
        # Write your code here

        m = len(M)

        if m == 0:
            return 0

        n = len(M[0])

        if n == 0:
            return 0

        res = 0

        # check rows
        for i in range(m):
            ll = 0
            for j in range(n):
                if M[i][j] == 1:
                    ll += 1
                else:
                    ll = 0

                if ll > res:
                    res = ll


        # check columns
        for i in range(n):
            ll = 0
            for j in range(m):
                if M[j][i] == 1:
                    ll += 1
                else:
                    ll = 0 
                if ll > res:
                    res = ll

        # check diagonals 
        dd = [[0] * n for i in range(m)]

        for i in range(m):
            if M[i][0] == 1:
                dd[i][0] = 1
                
        for i in range(n):
            if M[0][i] == 1:
                dd[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                if M[i][j] == 1:
                    dd[i][j] = M[i][j] * (dd[i - 1][j - 1] + 1)
                
                if dd[i][j] > res:
                    res = dd[i][j]
        
        # check off-diagonals
        oo = [[0] * n for i in range(m)]

        for i in range(m):
            if M[i][n - 1] == 1:
                oo[i][n - 1] = 1
                
        for i in range(n):
            if M[0][i] == 1:
                oo[0][i] = 1

        for i in range(1, m):
            for j in range(n - 2, -1, -1):
                if M[i][j] == 1:
                    oo[i][j] = M[i][j] * (oo[i - 1][j + 1] + 1)
                
                if oo[i][j] > res:
                    res = oo[i][j]

        return res 

if __name__ == '__main__':
    sol = Solution()
    print sol.longestLine([[0,0,0,0,0,1,1,0,1,0],[0,1,1,1,1,1,1,1,1,0],[0,1,1,0,1,0,1,1,1,1],[1,1,1,0,1,1,1,1,0,0],[1,1,0,0,1,1,0,0,1,0],[1,1,1,0,0,1,1,0,1,1],[1,0,1,1,0,1,0,0,1,1],[0,0,1,1,0,1,0,1,0,1],[1,1,1,1,1,1,0,0,1,1],[0,1,1,0,0,1,0,1,1,1]])
