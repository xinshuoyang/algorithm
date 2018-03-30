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

class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        
        if len(nums) <= 1:
            return nums

        #   forward traverse
        tmp1 = [1]

        for i in range(len(nums) - 1):
            tmp1.append(tmp1[-1] * nums[i])

        #   backward traverse
        tmp2 = [1]
        for i in range(len(nums) - 1, 0, -1):
            tmp2.append(tmp2[-1] * nums[i])

        #   get array B
        B = []
        for i in range(len(nums)):
            B.append(tmp1[i] * tmp2[len(nums) - i - 1])

        return B

if __name__ == '__main__':
    sol = Solution()
    print sol.productExcludeItself([1, 2, 3, 4, 5])
