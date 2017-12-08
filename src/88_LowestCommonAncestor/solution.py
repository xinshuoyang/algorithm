#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20171207
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
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here

        # find paths to A and B
        pathA = []
        pathB = []

        self.findpath(root, A, pathA)
        self.findpath(root, B, pathB)

        res = root

        for i in range(min(len(pathA), len(pathB))):
            if pathA[i] is pathB[i]:
                res = pathA[i]
            else:
                break

        return res 

    def findpath(self, root, node, path):
        """
        find path from root to node
        """

        if root is None:
            return False
        else:
            if root is node:
                path.append(root)
                return True
            else:
                found = False

                path.append(root)

                if root.left is not None:
                    found = self.findpath(root.left, node, path)

                if found:
                    return True

                if root.right is not None:
                    found = self.findpath(root.right, node, path)

                if found:
                    return True
                else:
                    path.pop()

                return False



if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)

    s = Solution()
    print s.lowestCommonAncestor(root, root.left, root.right.left).val
