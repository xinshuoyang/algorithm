#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20181222
#
################################################################################

class Solution:
    """
    @param A: The set A
    @param B: The set B
    @return: Return the size of three sets
    """
    def getAnswer(self, A, B):
        # Write your code here
        return [len(set(A).union(set(B))),len(set(A).intersection(set(B))),len(set(A).difference(set(B)))]
        
