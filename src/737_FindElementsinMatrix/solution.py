#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20171206
#
################################################################################

class Solution:
    """
    @param Matrix: the input
    @return: the element which appears every row
    """
    def FindElements(self, Matrix):
        # write your code here
        
        res = set(Matrix[0])

        for rr in Matrix:
            res = res.intersection(set(rr))

        return list(res)[0]
