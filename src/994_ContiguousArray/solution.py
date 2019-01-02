#!/usr/bin/python

##################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20190101
#
##################################################

class Solution:
    """
    @param nums: a binary array
    @return: the maximum length of a contiguous subarray
    """
    def findMaxLength(self, nums):
        # Write your code here
        if not nums:
            return 0

        maxsize = 0
        
        sumleft = [0]
        for i in range(len(nums)):
            if nums[i] is 1:
                sumleft.append(sumleft[-1]+1)
            else:
                sumleft.append(sumleft[-1]-1)
            if sumleft[-1] is 0:
                maxsize = i+1
        sumleft = sumleft[1:]
            
        d = dict.fromkeys(sumleft, -1) 
        for i in range(len(sumleft)):
            if d[sumleft[i]] is not -1:
                maxsize = max(maxsize, i-d[sumleft[i]])
            else:
                d[sumleft[i]] = i
        return maxsize 

if __name__ == "__main__":
    obj = Solution()
    print(obj.findMaxLength([0,0,0,0]))
