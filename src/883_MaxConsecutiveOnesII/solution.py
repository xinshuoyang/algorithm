#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180415
#
################################################################################

class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def findMaxConsecutiveOnes(self, nums):
        # write your code here

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        maxlen = 0
        l1 = 0
        l2 = 0
        flag = True

        for i in range(len(nums)):
            if nums[i] == 1:
                l2 += 1
                maxlen = max(l1 + l2 + 1, maxlen)
            else:
                flag = False

                l1 = l2
                l2 = 0

                maxlen = max(l1 + l2 + 1, maxlen)

        if flag:
            maxlen -= 1

        return maxlen

if __name__ == '__main__':
    sol = Solution()
    print sol.findMaxConsecutiveOnes([1,1,1,1])
