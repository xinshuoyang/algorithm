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
    @param root: the root node
    @param k: an integer
    @return: the number of nodes in the k-th layer of the binary tree
    """
    def kthfloorNode(self, root, k):
        return self.helper(k, root, 1)
        
    def helper(self, k, node, layer):
        if not node:
            return 0
        else:
            if k == layer:
                return 1
            elif k > layer:
                return self.helper(k, node.left, layer+1)+\
                        self.helper(k, node.right, layer+1)

if __name__ == "__main__":
    root = TreeNode(3)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    obj = Solution()
    print(obj.kthfloorNode(root, 2))
