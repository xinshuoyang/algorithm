#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20190123
#
################################################################################

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        if m <= 0:
            return 0
        if not A:
            return 0
        n = len(A)

        dp = [[0]*(m+1) for i in range(n)]
        
        for i in range(A[0], m):
            dp[0][i] = V[0]

        for i in range(1, n):
            dp[i][0] = 0
            for j in range(1, m+1):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                if j-A[i] >= 0:
                    dp[i][j] = max(dp[i][j],dp[i-1][j-A[i]]+V[i])
        
        print(dp)
        return dp[-1][-1]

if __name__ == "__main__":
    obj = Solution()
    print(obj.backPackII(100,[77,22,29,50,99],[92,22,87,46,90]))
    
