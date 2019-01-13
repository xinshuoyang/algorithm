#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20190112
#
################################################################################

class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        n = len(A)
        for i in range(n//2-1,-1,-1):
            self.helper(A,i,n)

    def helper(self,A,i,n):
        if 2*i+1 == n-1 and A[i] > A[2*i+1]:
            tmp = A[i]
            A[i] = A[2*i+1]
            A[2*i+1] = tmp
        elif 2*i+2 < n:
            if A[2*i+1] <= A[2*i+2]:
                if A[i] > A[2*i+1]:
                    tmp = A[i]
                    A[i] = A[2*i+1]
                    A[2*i+1] = tmp
                    self.helper(A,2*i+1,n)
            else:
                if A[i] > A[2*i+2]:
                    tmp = A[i]
                    A[i] = A[2*i+2]
                    A[2*i+2] = tmp
                    self.helper(A,2*i+2,n)
                    
if __name__ == "__main__":
    obj = Solution()
    print(obj.heapify([3,2,1,4,5]))
