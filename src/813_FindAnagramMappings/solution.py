#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20190104
#
################################################################################

class Solution:
    """
    @param A: lists A
    @param B: lists B
    @return: the index mapping
    """
    def anagramMappings(self, A, B):
        # Write your code here
        if not A or not B:
            return []
#        d = {}
#        for i in range(len(B)):
#            try:
#                d[B[i]].append(i)
#            except:
#                d[B[i]] = [i]

        d = {B[i]:i for i in range(len(B))}
        res = []    
        for i in range(len(A)):
            res.append(d[A[i]].pop())

        return res

if __name__ == "__main__":
    obj = Solution()
    print(obj.anagramMappings([84,8,0,84,0,84],[84,84,8,0,0,84]))

