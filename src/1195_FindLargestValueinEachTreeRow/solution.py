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

"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

#class Solution:
#    """
#    @param root: a root of integer
#    @return: return a list of integer
#    """
#    def largestValues(self, root):
#        # write your code here
#        vals = []
#        self.helper(root,0,vals)
#        return vals
#
#    def helper(self,node,level,vals):
#        if node != None:
#            if level > len(vals)-1:
#                vals.append(node.val)
#            else:
#                if node.val > vals[level]:
#                    vals[level] = node.val
#            self.helper(node.left,level+1,vals)
#            self.helper(node.right,level+1,vals)

class Solution:
    """
    @param root: a root of integer
    @return: return a list of integer
    """
    def largestValues(self, root):
        res = []
        layer = [root]

        while layer:
            newlayer = []

            res.append(layer[0].val)
            if layer[0].left:
                newlayer.append(layer[0].left)
            if layer[0].right:
                newlayer.append(layer[0].right)
            
            for i in range(1,len(layer)):
                if res[-1] < layer[i].val:
                    res[-1] = layer[i].val
                if layer[i].left:
                    newlayer.append(layer[i].left)
                if layer[i].right:
                    newlayer.append(layer[i].right)
            layer = newlayer

        return res
             
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)
    obj = Solution()
    print(obj.largestValues(root))
