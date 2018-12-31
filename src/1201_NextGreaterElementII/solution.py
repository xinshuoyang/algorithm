#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20181230
#
################################################################################

class Solution:
    """
    @param nums: an array
    @return: the Next Greater Number for every element
    """
    def nextGreaterElements(self, nums):
        # Write your code here
        m = len(nums)
        res = []
        for i in range(m):
            j = 1
            while j < m and nums[(i+j)%m] <= nums[i]:
                j += 1

            if j < m:
                res.append(nums[(i+j)%m])
            else:
                res.append(-1)
        return res

if __name__ == "__main__":
    obj = Solution()
    print(obj.nextGreaterElements([1,2,1,5,8,1,5,4,3,2,1]))
