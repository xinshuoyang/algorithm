#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180423
#
################################################################################

class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        
        if len(A) == 0:
            return [-1, -1]

        first = 0
        last = len(A) - 1

        found = False
        
        while first + 1 < last:
            mid = first + (last - first) / 2

            if A[mid] == target:
                found = True
                break
            elif A[mid] > target:
                last = mid
            else:
                first = mid
        
        if found:
            p1 = mid
            p2 = mid

            while p1 > 0:
                if A[p1 - 1] == target:
                    p1 -= 1
                else:
                    break

            while p2 < len(A) - 1:
                if A[p2 + 1] == target:
                    p2 += 1
                else:
                    break

            return [p1, p2]

        if A[first] == target and A[last] == target:
            return [first, last]

        if A[fisrt] == target:
            return [first, first]

        if A[last] == target:
            return [last, last]

        return [-1, -1]




if __name__ == '__main__':
    sol = Solution()
    A = []
    target = 9 
    print sol.searchRange(A, target)
