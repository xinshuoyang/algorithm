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
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        res = []
        self.helper(root,target,[],res)
        return res
        
    def helper(self, node, target, path, pathlist):
        if node != None:
            if not node.left and not node.right:
                if node.val == target:
                    path.append(node.val)
                    pathlist.append(path)
            else:
                self.helper(node.left,target-node.val,path+[node.val],pathlist)
                self.helper(node.right,target-node.val,path+[node.val],pathlist)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(3)

    ss = Solution()
    print(ss.binaryTreePathSum(root, 5))
