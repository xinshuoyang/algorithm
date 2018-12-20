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
    @param nums1: an array
    @param nums2: an array
    @return:  find all the next greater numbers for nums1's elements in the corresponding places of nums2
    """
    def nextGreaterElement(self, nums1, nums2):
        # Write your code here
        if len(nums2) == 0:
            return []
            
        if len(nums2) == 1:
            return [-1]

        ref = [-1]*len(nums2)
        maxnum = nums2[-1]
        for i in range(len(nums2)-2,-1,-1):
            if nums2[i] < maxnum:
                for j in range(i,len(nums2)):
                    if nums2[i] < nums2[j]:
                        ref[i] = nums2[j]
                        break
            else:
                ref[i] = -1

            if nums2[i] > maxnum:
                maxnum = nums2[i]

        res = []
        for i in range(len(nums1)):
            res.append(ref[nums2.index(nums1[i])])

        return res

if __name__ == "__main__":
    ss = Solution()
    print ss.nextGreaterElement([4,1,2],[1,3,4,2])
