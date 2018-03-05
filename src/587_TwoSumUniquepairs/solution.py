#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180304
#
################################################################################

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here

        if len(nums) <= 1:
            return 0
        
        s1 = sorted(nums)

        p1 = 0
        p2 = len(s1) - 1


        res = 0
        while p1 < p2:
            if s1[p1] + s1[p2] <= target:
                if s1[p1] + s1[p2] == target:
                    res += 1
                p1 += 1

                if p1 + 1 < len(s1):
                    while s1[p1] == s1[p1 - 1]:
                        p1 += 1
            else:
                p2 -= 1

        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.twoSum6([7,11,11,1,2,3,4], 22)
