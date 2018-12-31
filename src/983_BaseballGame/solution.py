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
    @param ops: the list of operations
    @return:  the sum of the points you could get in all the rounds
    """
    def calPoints(self, ops):
        # Write your code here
        stack = []
        while ops:
            pp = ops.pop(0)
            if pp is "+":
                stack.append(stack[-1]+stack[-2])
            elif pp is "D":
                stack.append(stack[-1]*2)
            elif pp is "C":
                stack.pop()
            else:
                stack.append(int(pp))
        return sum(stack)

if __name__ == "__main__":
    obj = Solution()
    print(obj.calPoints(["5","-2","4","C","D","9","+","+"]))
