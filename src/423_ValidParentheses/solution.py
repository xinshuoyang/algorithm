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
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        stack1 = list(s)
        stack2 = []
        left = ["(","{","["]
        right = [")","}","]"]
        
        while stack1:
            pp = stack1.pop()
            if pp in right:
                stack2.append(pp)
            else:
                if not stack2:
                    return False
                else:
                    qq = stack2.pop()
                    if not self.isPair(pp,qq):
                        return False
        if stack2:
            return False
        return True

    def isPair(self,pp,qq):
        if pp is "(":
            if qq is ")":
                return True
        if pp is "{":
            if qq is "}":
                return True
        if pp is "[":
            if qq is "]":
                return True
        return False

if __name__ == "__main__":
    obj = Solution()
    print(obj.isValidParentheses("]"))
