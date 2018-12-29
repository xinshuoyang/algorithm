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
    @param root: t
    @return: the sum of all left leaves
    """
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        else:
            if not root.left:
                return self.sumOfLeftLeaves(root.right)
            else:
                if not root.left.left and not root.left.right:
                    return root.left.val+self.sumOfLeftLeaves(root.right)
                else:
                    return self.sumOfLeftLeaves(root.left)+\
                            self.sumOfLeftLeaves(root.right)

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    obj = Solution()
    print(obj.sumOfLeftLeaves(root))
                
