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
    @param root: root of the given tree
    @return: whether it is a mirror of itself 
    """
    def isSymmetric(self, root):
        return self.helper(root.left, root.right)
    
    def helper(self,node1,node2):
        if node1 == None and node2 == None:
            return True
        elif node1 == None and node2 != None:
            return False
        elif node1 != None and node2 == None:
            return False
        else:
            if node1.val != node2.val:
                return False
            else:
                return self.helper(node1.left,node2.right) and\
                        self.helper(node1.right,node2.left)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    #root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    #root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    obj = Solution()
    print(obj.isSymmetric(root))
