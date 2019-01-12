#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20190111
#
################################################################################
class ListNode:
    def __init__(self,num):
        self.val = num
        self.next = None
        
class MyQueue:
    """
    Initialization
    """
    def __init__(self):
        self.head,self.last = None,None
        
    """
    @param: item: An integer
    @return: nothing
    """
    def enqueue(self, item):
        # write your code here
        if not self.head:
            self.head = ListNode(item)
            self.last = self.head
        else:
            self.last.next = ListNode(item)
            self.last = self.last.next

    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        if not self.head:
            return None
        else:
            res = self.head.val
            self.head = self.head.next
            return res

