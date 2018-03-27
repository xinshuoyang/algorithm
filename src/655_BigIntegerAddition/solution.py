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
    @return: return sum of num1 and num2
    """
    def addStrings(self, num1, num2):
        # write your code here

        setdig = False
        
        l1 = len(num1)
        l2 = len(num2)

        res = ''
        
        d = 1 
        
        while d <= l1 or d <= l2:

            if d <= l1 and d <= l2:
                d1 = int(num1[-d])
                d2 = int(num2[-d])

                if setdig:
                    s = d1 + d2 + 1
                else:
                    s = d1 + d2

                if s >= 10:
                    res = str(s % 10) + res
                    setdig = True
                else:
                    res = str(s) + res
                    setdig = False

            elif d <= l1 and d > l2:
                d1 = int(num1[-d])

                if setdig:
                    s = d1 + 1
                else:
                    s = d1

                if s >= 10:
                    res = str(s % 10) + res
                    setdig = True
                else:
                    res = str(s) + res
                    setdig = False
            elif d > l1 and d <= l2:

                d2 = int(num2[-d])

                if setdig:
                    s = d2 + 1
                else:
                    s = d2

                if s >= 10:
                    res = str(s % 10) + res
                    setdig = True
                else:
                    res = str(s) + res
                    setdig = False
            d += 1
        
        if setdig:
            res = '1' + res

        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.addStrings("187182781728","1298912891289189189898198291")
