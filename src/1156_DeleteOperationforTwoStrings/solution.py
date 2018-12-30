#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20181229
#
################################################################################

class Solution:
    """
    @param word1: a string
    @param word2: a string
    @return: return a integer
    """
    def minDistance(self, word1, word2):
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)

        dp = [[0 for i in range(len(word1))] for j in range(len(word2))]
        for i in range(len(word1)):
            if word2[0] in word1[:i+1]:
                dp[0][i] = 1
        for i in range(len(word2)):
            if word1[0] in word2[:i+1]:
                dp[i][0] = 1
        
        for i in range(1,len(word1)):
            for j in range(1,len(word2)):
                if word1[i] == word2[j]:
                    dp[j][i] = dp[j-1][i-1]+1
                else:
                    dp[j][i] = max(dp[j-1][i-1],dp[j-1][i],dp[j][i-1])
        return len(word1)+len(word2)-2*dp[-1][-1]
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.minDistance("horse","ros"))
    #print(obj.minDistance("sea","eat"))
    
