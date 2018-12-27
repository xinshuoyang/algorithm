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
import numpy as np
class Solution:
    """
    @param n: the value from 1 - n
    @param value: the value of coins
    @param amount: the number of coins
    @return: how many different value
    """
#    def backPackVIII(self, n, value, amount):
#        if n == 0 or not value or not amount:
#            return 0
#        
#        idx = sorted(range(len(value)), key=value.__getitem__)
#        val = [value[i] for i in idx]
#        amo = [amount[i] for i in idx]
#        
#        dp1 = [False]*n
#        dp1[val[0]-1] = True
#        amo[0] -= 1
#        
#        tset = set()
#        tset.add(val[0]-1)
#        
#        for i in range(len(amo)):
#            dp2 = [False]*n
#            for k in range(n):
#                if dp1[k] or val[i] == k+1:
#                    dp2[k] = True
#                    tset.add(k)
#                else:
#                    if val[i] > k+1:
#                        dp2[k] = False
#                    else:
#                        dp2[k] = dp1[k-val[i]]
#                        if dp2[k]:
#                            tset.add(k)
#            
#            for j in range(1, amo[i]):
#                newset = set()
#                for k in tset:
#                    if k+val[i] < n:
#                        newset.add(k+val[i])
#                tset = tset.union(newset)
#
#            dp1 = [False]*n
#            for k in tset:
#                dp1[k] = True
#        
#        return sum(dp1)

    def backPackVIII(self, n, value, amount):
        if n == 0 or not value or not amount:
            return 0
        
        tset = set()
        tset.add(0)
        
        for i in range(len(amount)):
            for j in range(amount[i]):
                newset = set()
                for k in tset:
                    if k+value[i] < n:
                        newset.add(k+value[i])
                tset = tset.union(newset)

        #dp = [False]*n
        #for k in tset:
        #    dp[k] = True
        return len(tset)-1 
        #return sum(dp)    
if __name__ == "__main__":
    ss = Solution()
    #print(ss.backPackVIII(10,[2],[5]))
    print(ss.backPackVIII(9069,[880,548,836,568,525,605,198,187,290,286,551,247,52,428,119,101,62,591,416,369],[690,572,719,592,402,453,829,73,458,853,538,255,548,520,520,310,780,806,91,143]))
                        

