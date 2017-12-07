#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20171206
#
################################################################################

"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

"""
Definition for singly-linked list.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if not root:
            return None
        else:
            res = []
            self.bfs(root, res)

            return res

    def bfs(self, root, nodes):
        
        q1 = [root]

        while len(q1) != 0:
            q2 = []

            head = ListNode(q1[0].val)
            nodes.append(head)

            if q1[0].left != None:
                q2.append(q1[0].left)
            if q1[0].right != None:
                q2.append(q1[0].right)
            
            for i in range(1, len(q1)):
                head.next = ListNode(q1[i].val)
                head = head.next

                if q1[i].left != None:
                    q2.append(q1[i].left)

                if q1[i].right != None:
                    q2.append(q1[i].right)
            
            q1 = q2

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    s = Solution()
    nodes = s.binaryTreeToLists(root)
    
    for node in nodes:
        print node.val
