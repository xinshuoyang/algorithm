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

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param t1: the root of the first tree
    @param t2: the root of the second tree
    @return: the new binary tree after merge
    """
    def mergeTrees(self, t1, t2):
        # Write your code here
        if t1 == None and t2 == None:
            return None
        else:
            if t1 == None:
                root = TreeNode(t2.val)
                root.left = self.mergeTrees(t2.left, None)
                root.right = self.mergeTrees(t2.right, None)
                return root
            elif t2 == None:
                root = TreeNode(t1.val)
                root.left = self.mergeTrees(t1.left, None)
                root.right = self.mergeTrees(t1.right, None)
                return root 
            else:
                root = TreeNode(t1.val+t2.val)
                root.left = self.mergeTrees(t1.left, t2.left)
                root.right = self.mergeTrees(t1.right, t2.right)
                return root


