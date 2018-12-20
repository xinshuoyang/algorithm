#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180323
#
################################################################################

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        if len(nums) <= 1:
            return 0

        np = 0
        snums = sorted(nums)
        print snums
        
        p1 = len(snums) - 1
        p2 = p1 - 1

        if snums[p1] + snums[p2] <= target:
            return 0
        while p2 >= 0 and snums[p1] + snums[p2] > target:
            p2 -= 1
        p2 += 1

        np = p1 - p2

        p1 -= 1

        while p1 > p2: 
            while p1 > p2 and snums[p1] + snums[p2] <= target:
                p2 += 1
            np += p1 - p2
            p1 -= 1
        return np
            

if __name__ == '__main__':
    sol = Solution()
    print sol.twoSum2([1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99], -64)
