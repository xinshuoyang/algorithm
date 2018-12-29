#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20181228
#
################################################################################

################################################################################
#
#   Python2
#   Written by X. Yang
#   DATE: 2017
#
################################################################################
#"""
#Definition of TreeNode:
#class TreeNode:
#    def __init__(self, val):
#        self.val = val
#        self.left, self.right = None, None
#"""
#class Solution:
#    """
#    @param root: The root of binary tree.
#    @return: Level order in a list of lists of integers
#    """
#    def levelOrder(self, root):
#        # write your code here
#        trav = []
#        self.TravDepth(root, trav, 0)
#        return trav
#        
#    def TravDepth(self, root, trav, lvl):
#        if root == None:
#            return
#        else:
#            if len(trav) < lvl+1:
#                trav += [[]]
#            trav[lvl] += [root.val]
#            
#            self.TravDepth(root.left, trav, lvl+1)
#            self.TravDepth(root.right, trav, lvl+1)

################################################################################
#
#   Written by X. Yang
#
#   DATE: Dec. 2018
#
################################################################################
"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        nodelist = []
        self.helper(root,0,nodelist)
        return nodelist
    
    def helper(self, node, level, nodelist):
        if not node:
            return
        else:
            if len(nodelist) <= level:
                nodelist.append([node.val])
            else:
                nodelist[level].append(node.val)
            self.helper(node.left,level+1,nodelist)
            self.helper(node.right,level+1,nodelist)

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    ss = Solution()
    print(ss.levelOrder(root))
