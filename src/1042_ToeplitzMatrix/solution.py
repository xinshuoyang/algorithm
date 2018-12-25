#!/usr/bin/python

##################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20181224
#
##################################################

class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """
    def isToeplitzMatrix(self, matrix):
        # Write your code here

        m = len(matrix)
        if m == 0:
            return True

        n = len(matrix[0])
        if n == 0:
            return True
        print m, n
        for i in range(m):
            val = matrix[i][0]
            print val
            for j in range(1,min(m-i,n)):
                print matrix[i+j][j]
                if matrix[i+j][j] != val:
                    return False
        for i in range(n):
            val = matrix[0][i]
            for j in range(1,min(m,n-i)):
                if matrix[j][i+j] != val:
                    return False

        return True

if __name__ == "__main__":
    ss = Solution()
    print ss.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
