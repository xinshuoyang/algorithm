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

class Solution:
    """
    @param root: the root of the tree
    @return: the total sum of all root-to-leaf numbers
    """
    def sumNumbers(self, root):
        return self.helper(root,[])
    
    def helper(self,node,prev):
        if not node:
            return 0
        else:
            if not node.left and not node.right:
                sums = 0
                for i in range(len(prev)):
                    sums += prev[i]*10**(len(prev)-i)
                sums += node.val
                return sums
            else:
                return self.helper(node.left,prev+[node.val])+\
                        self.helper(node.right,prev+[node.val])

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(0)
    #root.right = TreeNode(3)
    
    ss = Solution()
    print(ss.sumNumbers(root))
