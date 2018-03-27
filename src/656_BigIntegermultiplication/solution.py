#!/usr/bin/python

##################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180325
#
##################################################

class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return product of num1 and num2
    """
    def multiply(self, num1, num2):
        # write your code here

        l1 = len(num1)
        l2 = len(num2)
        
        if l1 == 1:
            if num1 == '0':
                return '0'

        if l2 == 1:
            if num2 == '0':
                return '0' 

        dig = {}

        for d1 in range(1, l1 + 1):
            for d2 in range(1, l2 + 1):
                if dig.has_key(d1 + d2 - 1):
                    dig[d1 + d2 - 1] += int(num1[-d1]) * int(num2[-d2])
                else:
                    dig[d1 + d2 - 1] = int(num1[-d1]) * int(num2[-d2])

        res = ''

        setdig = 0

        for d in sorted(dig.keys()):
            ss = dig[d] + setdig
            res =  str(ss % 10) + res
            setdig = ss / 10

        if setdig > 0:
            res = str(setdig) + res

        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.multiply('99', '999')
