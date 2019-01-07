#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20190107
#
################################################################################

class Solution:
    """
    @param n: an integer
    @return: the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n
    """
    def nextGreaterElement(self, n):
        # Write your code here
        digits = [int(i) for i in list(str(n))]
        nd = len(digits)
        if nd is 1:
            return n
        maxval = 2**31-1
        for i in range(nd-2,-1,-1):
            for j in range(nd-1,i-1,-1):
                if digits[i] < digits[j]:
                    temp = digits[i]
                    digits[i] = digits[j]
                    digits[j] = temp
                    newdigits = digits[:i+1]+sorted(digits[i+1:])
                    res = 0
                    for k in range(len(newdigits)):
                        res += newdigits[k]*10**(len(newdigits)-k-1)
                        if res > maxval:
                            return -1
                    return res
        return -1
        
if __name__ == "__main__":
    obj = Solution()
    print(obj.nextGreaterElement(1999999999))
