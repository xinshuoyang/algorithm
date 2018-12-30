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


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self, ):
        # write your code here
        return len(self.stack)

    """
    @return: return next node
    """
    def next(self, ):
        # write your code here
        node = self.stack.pop()
        n = node.right

        while n:
            self.stack.append(n)
            n = n.left
        return node

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(1)
    root.right = TreeNode(11)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(12)

    obj = BSTIterator(root)
    while obj.hasNext():
        print(obj.next().val)
