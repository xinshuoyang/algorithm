#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20190115
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
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        # write your code here
        if not root:
            return []

        res = []
        while root.left or root.right:
            vals = []
            self.helper(root,vals)
            res.append(vals)
        res.append([root.val])
        return res

    def helper(self, node, vals):
        if node:
            if node.left:
                if not node.left.left and not node.left.right:
                    vals.append(node.left.val)
                    node.left = None
                else:
                    self.helper(node.left, vals)
            if node.right:
                if not node.right.left and not node.right.right:
                    vals.append(node.right.val)
                    node.right = None
                else:
                    self.helper(node.right,vals)

if __name__ == "__main__":
    obj = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(obj.findLeaves(root))
