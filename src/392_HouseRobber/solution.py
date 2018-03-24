#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180323
#
################################################################################
class Solution:
    """
    @param: A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        # write your code here
        if len(A) == 0:
            return 0

        if len(A) <= 2:
            return max(A)
        
        v1 = A[0]
        v2 = max(A[:2])

        for i in range(2, len(A)):
            temp = v2
            v2 = max(v2, A[i] + v1)
            v1 = temp

        return v2



if __name__ == '__main__':
    sol = Solution()
    A = [828,125,740,724,983]
    print sol.houseRobber(A)

