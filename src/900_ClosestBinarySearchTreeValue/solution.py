#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20181230
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
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        closest = root.val
        while root:
            if abs(root.val-target) < abs(target-closest):
                closest = root.val
            
            if root.val > target:
                root = root.left
            elif root.val < target:
                root = root.right
        return closest

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(1)
    target = 4.142857
    obj = Solution()
    print(obj.closestValue(root, target))
