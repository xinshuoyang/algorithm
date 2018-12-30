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
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        vals = []
        self.helper(root,vals,k)
        return vals[k-1]

    def helper(self,node,vals,k):
        if len(vals) >= k:
            return
        if node:
            if not node.left and not node.right:
                vals.append(node.val)
            else:
                self.helper(node.left,vals,k)
                vals.append(node.val)
                self.helper(node.right,vals,k)
        
if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)

    obj = Solution()
    print(obj.kthSmallest(root, 2))
