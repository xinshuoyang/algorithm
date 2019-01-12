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
    def __init__(self,val):
        self.val = val
        self.next = None

class Dequeue:
    
    def __init__(self):
        # do intialization if necessary
        self.head,self.ass = None,None

    """
    @param: item: An integer
    @return: nothing
    """
    def push_front(self, item):
        # write your code here
        if not self.head:
            self.head = ListNode(item)
            self.ass = self.head
        else:
            oldhead = self.head
            self.head = ListNode(item)
            self.head.next = oldhead

    """
    @param: item: An integer
    @return: nothing
    """
    def push_back(self, item):
        # write your code here
        if not self.head:
            self.head = ListNode(item)
            self.ass = self.head
        else:
            self.ass.next = ListNode(item)
            self.ass = self.ass.next
        
    """
    @return: An integer
    """
    def pop_front(self):
        # write your code here
        if not self.head:
            return None
        else:
            res = self.head.val
            if not self.head.next:
                self.ass = None
            self.head = self.head.next
            return res

    """
    @return: An integer
    """
    def pop_back(self):
        # write your code here
        if not self.ass:
            return None
        else:
            res = self.ass.val
            if not self.head.next:
                self.head = None
                self.ass = None
            else: 
                node = self.head
                while node.next.next:
                    node = node.next
                node.next = None
                self.ass = node
            return res

if __name__ == "__main__":
    obj = Dequeue()
    obj.push_front(1)
    obj.push_back(2)
    print(obj.pop_back())
    print(obj.pop_back())
    obj.push_back(3)
    obj.push_back(4)
    print(obj.pop_front())
    print(obj.pop_front())
