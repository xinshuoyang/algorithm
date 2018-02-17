#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180217
#
################################################################################

"""
Definition of ListNode
"""

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param: node: a list node in the list
    @param: x: An integer
    @return: the inserted new list node
    """
    def insert(self, node, x):
        # write your code here

        if node == None:
            node = ListNode(x)
            node.next = node
            return node


        prev = None
        p = node

        while True:
            prev = p
            p = p.next

            if x >= prev.val and x <= p.val:
                break
            
            if (prev.val > p.val) and (x > prev.val or x < p.val):
                break

            if p == node:
                break

        newnode = ListNode(x)
        prev.next = newnode
        newnode.next = p

        return newnode

       




if __name__== '__main__':

    s = Solution()
    res = s.insert(None, 4)
    print res.val
