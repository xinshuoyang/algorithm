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
Definition for a binary tree node.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        stack = []
        while root:
            stack.append(root)
            root = root.left
        
        nxt = False
        while stack:
            node = stack.pop()
            
            if nxt:
                return node
            if node == p:
                nxt = True

            right = node.right
            while right:
                stack.append(right)
                right = right.left

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    obj = Solution()
    print(obj.inorderSuccessor(root, root).val)
