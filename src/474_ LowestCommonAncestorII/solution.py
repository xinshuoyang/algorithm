"""
Definition of ParentTreeNode:
"""
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here

        # find paths from A and B to root
        pathA = []
        pathB = []

        self.findpath(root, A, pathA)
        self.findpath(root, B, pathB)

        res = root

        for i in range(-1, - min(len(pathA), len(pathB)) - 1, -1):
            if pathA[i] is pathB[i]:
                res = pathA[i]
            else:
                break

        return res

    def findpath(self, root, node, path):
        """
        find path from node to root
        """

        if node is root:
            path.append(node)
        else:
            path.append(node)
            self.findpath(root, node.parent, path)

if __name__ == '__main__':

    root = ParentTreeNode(4)
    root.left = ParentTreeNode(3)
    root.right = ParentTreeNode(7)
    root.right.left = ParentTreeNode(5)
    root.right.right = ParentTreeNode(6)
    root.right.right.parent = root.right
    root.right.left.parent = root.right
    root.left.parent = root
    root.right.parent = root

    s = Solution()

    print s.lowestCommonAncestorII(root, root.right.left, root.left).val