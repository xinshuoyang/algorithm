#!/usr/bin/python

##################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180328
#
##################################################

"""
Definition for singly-linked list.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    @param: head: a ListNode
    @param: val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        # write your code here

        # find new head
        while head != None:
            if head.val == val:
                head = head.next
            else:
                break

        p1 = head
        if p1 != None:
            p2 = p1.next
        else:
            p2 = None

        while p2 != None:
            if p2.val == val:
                p2 = p2.next
                p1.next = p2
            else:
                p1 = p2
                p2 = p2.next
               
        return head 

if __name__ == '__main__':
    sol = Solution()
    print sol.removeElements(None, 2)
