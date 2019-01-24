#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20190120
#
################################################################################

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        snums = sorted(numbers)
        
        res = sum(numbers[0:3])
        diff = abs(res-target)
        for i in range(len(snums)-2):
            dd, ss = self.twoSumClosest(snums[i+1:], target-snums[i])
            if dd < diff:
                diff = dd
                res = ss+snums[i]
        return res

    def twoSumClosest(self, nums, target):
        p1 = 0
        p2 = len(nums)-1
        
        diff = abs(nums[0]+nums[1]-target)
        res = nums[0]+nums[1]
        
        while p1 < p2:
            if nums[p1]+nums[p2] == target:
                return 0, nums[p1]+nums[p2]
            elif nums[p1]+nums[p2] > target:
                if diff > nums[p1]+nums[p2]-target:
                    diff = nums[p1]+nums[p2]-target
                    res = nums[p1]+nums[p2]
                p2 -= 1
            else:
                if diff > target-nums[p1]-nums[p2]:
                    diff = target-nums[p1]-nums[p2]
                    res = nums[p1]+nums[p2]
                p1 += 1
        return diff, res

if __name__ == "__main__":
    obj = Solution()
    print(obj.threeSumClosest([-5,-3,-2,1,2,2,3,4,9], 1))
