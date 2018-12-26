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
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        if not A or not V or m == 0:
            return 0
        
        dd = dict()
        for i in range(len(A)):
            dd[A[i]] = V[i]
            
        dp = [0]*min(A)+[V[A.index(min(A))]]
        
        for i in range(min(A)+1, m+1):
            if i in dd.keys():
                dp.append(dd[i])
            else:
                dp.append(0)
             
            for j in range(len(A)):
                if A[j] < i:
                    dp[i] = max(dp[i],dp[i-A[j]]+V[j])
            #for j in range(1,i//2+1):
            #    dp[i] = max(dp[i],dp[j]+dp[i-j])
        print(dp)
        return dp[m]


if __name__=="__main__":
    ss = Solution()
    ss.backPackIII([79,58,86,11,28,62,15,68],[83,14,54,79,72,52,48,62],200)
