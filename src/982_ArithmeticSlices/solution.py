#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20190110
#
################################################################################

class Solution:
    """
    @param A: an array
    @return: the number of arithmetic slices in the array A.
    """
    def numberOfArithmeticSlices(self, A):
        # Write your code here
        diff = []
        for i in range(1,len(A)):
            diff.append(A[i]-A[i-1])

        length = []
        ll = 1
        for i in range(len(diff)-1):
            if diff[i] == diff[i+1]:
                ll += 1
            else:
                if ll+1 >= 3:
                    length.append(ll+1)
                ll = 1
        if ll+1 >= 3:
            length.append(ll+1)

        print(length)
        res = 0
        for i in range(len(length)):
            res += (length[i]-1)*(length[i]-2)//2
        return res

if __name__ == "__main__":
    obj = Solution()
    print(obj.numberOfArithmeticSlices([1,3,5,7,9,2,4,6,8,10,3,2,3,5]))
