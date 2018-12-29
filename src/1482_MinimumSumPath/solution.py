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
    @param root: the root
    @return: minimum sum
    """
    def minimumSum(self, root):
        if not root:
            return 0
        sums = []
        self.helper(root,0,sums)
        return min(sums)

        
    def helper(self,node,prev,sums):
        if node != None:
            if not node.left and not node.right:
                sums.append(prev+node.val)
            else:
                self.helper(node.left,prev+node.val,sums)
                self.helper(node.right,prev+node.val,sums)

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(8)

    obj = Solution()
    print(obj.minimumSum(root))

