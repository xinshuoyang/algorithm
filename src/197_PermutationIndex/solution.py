#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180330
#
################################################################################
import math
class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        # write your code here
        
        if len(A) == 1:
            return 1

        SA = sorted(A)
        
        i = 0
        index = 0

        while i < len(A):
            for j in range(len(SA)):
                if A[i] == SA[j]:
                    SA.pop(j)
                    break
                else:
                    index += math.factorial(len(A) - 1 - i)
            i += 1
        return index + 1


if __name__ == '__main__':
    sol = Solution()
    print sol.permutationIndex([4, 2, 3, 1, 9])

