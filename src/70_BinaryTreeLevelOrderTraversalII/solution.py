#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20171205
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
    @param: root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code here

        if not root:
            return []
        else:
            nodes = []

            self.bfs(root, nodes)
            
            return nodes

    def bfs(self, root, nodes):

        q1 = [root]

        while q1:

            q2 = []

            ll = []

            for node in q1:
                ll.append(node.val)

                if node.left != None:
                    q2.append(node.left)

                if node.right != None:
                    q2.append(node.right)
           
            nodes.insert(0, ll)

            q1 = q2

if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print s.levelOrderBottom(root)

