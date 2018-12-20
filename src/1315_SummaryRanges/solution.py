#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20181219
#
################################################################################

class Solution:
    """
    @param nums:  a sorted integer array without duplicates
    @return: the summary of its ranges
    """
    def summaryRanges(self, nums):
        # Write your code here
        
        if len(nums) == 0:
            return []
        res = []
        i = 0
        while i < len(nums):
            
            start = nums[i]

            j = i
            
            while j+1 < len(nums) and nums[j]+1 == nums[j+1]:
                j += 1
            stop = nums[j]
            
            if start == stop:
                res.append(str(start))
            else:
                res.append(str(start)+"->"+str(stop))
            
            i = j+1
                
        return res

if __name__ == '__main__':
    ss = Solution()
    print ss.summaryRanges([0,1])
