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
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        
        serialization = ''

        q1 = [root]

        while q1:
            q2 = []
            
            for node in q1:
                if node != None:
                    serialization += str(node.val) + ' '
                    q2.append(node.left)
                    q2.append(node.right)
                else:
                    serialization += '# '
           
            q1 = q2
                  
        return serialization

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        
        if len(data) == 0:
            return None
        
        vals = []
        for i in data.split(' '):
            if i != '':
                vals.append(i)
        
        if vals[0] == '#':
            return None
        
        root = TreeNode(vals[0])

        q1 = [root]
        p = 1
        
        while q1:
            q2 = []

            for node in q1:
                if vals[p] != '#':
                    node.left = TreeNode(vals[p])
                    q2.append(node.left)

                if vals[p + 1] != '#':
                    node.right = TreeNode(vals[p + 1])
                    q2.append(node.right)
                p += 2
            q1 = q2

        return root

        
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    
    root.left.left = TreeNode(3)

    root.left.left.left = TreeNode(4)
    s = Solution()
    serialization = s.serialize(root)

    root = s.deserialize(serialization)

    print root.val
    print root.right
    print root.left.val
    print root.left.left.val
    print root.left.left.left.val
