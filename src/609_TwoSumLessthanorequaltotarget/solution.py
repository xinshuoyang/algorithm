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
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here

        if len(nums) <= 1:
            return 0
        
        snums = sorted(nums)

        p1 = 0
        p2 = len(nums) - 1

        res = 0
        while p1 != p2:
            if snums[p1] + snums[p2] <= target:
                res += p2 - p1
                p1 += 1
            else:
                p2 -= 1
                
        return res 

if __name__ == '__main__':
    sol = Solution()
    print sol.twoSum5([2, 7, 11, 15], 17)
