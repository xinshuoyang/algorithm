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
    @param num: The arry you should handle
    @return: Return the array
    """
    def getPreviousNumber(self, num):
        # Write your code here
        stack = []
        res = []
        for i in range(len(num)):
            while len(stack)>0 and stack[-1]>=num[i]:
                stack.pop()

            if len(stack) > 0:
                res.append(stack[-1])
            else:
                res.append(num[i])
            
            stack.append(num[i])
        return res

if __name__ == "__main__":
    obj = Solution()
    print(obj.getPreviousNumber([6,3,1,2,5,10,9,15]))
