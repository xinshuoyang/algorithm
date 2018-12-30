#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20181229
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
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        vals = []
        self.helper(root, vals)
        for i in range(1,len(vals)):
            if vals[i-1] >= vals[i]:
                return False
        return True

    def helper(self, root, vals):
        if root:
            if root.left:
                self.helper(root.left, vals)
            vals.append(root.val)
            if root.right:
                self.helper(root.right, vals)



if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(100)

    obj = Solution()
    print(obj.isValidBST(root))
