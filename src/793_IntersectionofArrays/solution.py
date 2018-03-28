#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180327
#
################################################################################
class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # write your code here
        if len(arrs) <= 1:
            return 0

        temp = sorted(arrs[0])
        for i in range(1, len(arrs)):
            temp = self.intersect(temp, sorted(arrs[i]))
            if temp == []:
                return 0

        return len(temp)


    def intersect(self, A, B):
        """
        find the intersection of two sorted arraries A and B
        """
        
        la = len(A)
        lb = len(B)

        if la == 0 or lb == 0:
            return []

        if A[-1] < B[0] or B[-1] < A[0]:
            return []

        intersection = []

        p1 = 0
        p2 = 0

        while p1 < la and p2 < lb:
            if A[p1] == B[p2]:
                intersection.append(A[p1])
                p1 += 1
                p2 += 1
            elif A[p1] < B[p2]:
                p1 += 1
            else:
                p2 += 1

        return intersection

if __name__ == '__main__':
    sol = Solution()
    print sol.intersectionOfArrays([[1,2,3,4],[1,2,5,6,7], [9,10,1,5,2,3]])
