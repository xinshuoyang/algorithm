#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180402
#
################################################################################

class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        
        if len(nums) == 0:
            return 0

        res = 0
        pp = 0
        counts = 1
        
        while pp < len(nums):

            if pp + 1 < len(nums):
                if nums[pp + 1] == nums[pp]:
                    counts += 1
                else:
                    if counts >= 2:
                        nums[res] = nums[pp]
                        nums[res + 1] = nums[pp]
                        res += 2
                    else:
                        nums[res] = nums[pp]
                        res += 1
                    
                    counts = 1
            else:
                if counts >= 2:
                    nums[res] = nums[pp]
                    nums[res + 1] = nums[pp]
                    res += 2
                else:
                    nums[res] = nums[pp]
                    res += 1

            pp += 1
        
        return res


if __name__ == '__main__':
    sol = Solution()
    #nums = [-14,-14,-14,-14,-14,-14,-14,-13,-13,-13,-13,-12]
    nums = [-14,-14,-14,-14,-14,-14,-14,-13,-13,-13,-13,-12,-11,-11,-11,-9,-9,-9,-7,-7,-7,-6,-6,-5,-5,-5,-4,-4,-4,-3,-3,-3,-2,-2,-2,-1,-1,0,0,0,0,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,5,5,6,6,6,7,7,7,7,8,8,8,8,9,9,10,10,11,11,11,11,11,12,12,12,12,13,13,13,13,14,14,15,16,17,18,18,18,20,20,21,21,21,21,21,22,22,22,22,23,24,24, 25]
    ll = sol.removeDuplicates(nums)
    print nums[0:ll], ll
