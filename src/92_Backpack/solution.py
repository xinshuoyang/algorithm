#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20181226
#
################################################################################

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        if not A or m == 0:
            return 0
        if m > sum(A):
            return sum(A)

        dp = [[0]*(len(A)+1) for i in range(m+1)]
        
        A = sorted(A)
        for i in range(len(A)):
            dp[A[0]][i+1] = A[0]
        for i in range(A[0]+1,m+1):
            dp[i][1] = A[0]

        for i in range(A[0]+1, m+1):
            for j in range(1, len(A)):
                if i < A[j]:
                    dp[i][j+1] = dp[i][j]
                elif i == A[j]:
                    dp[i][j+1] = A[j]
                else:
                    dp[i][j+1] = max(dp[i][j], dp[i-A[j]][j]+A[j])

        return dp[m][len(A)]

if __name__ == "__main__":
    ss = Solution()
    print ss.backPack(10, [20,15,15,15,15,15,15,15,15,15,15,15,15,15,15,7,2,15,15,15,15])
