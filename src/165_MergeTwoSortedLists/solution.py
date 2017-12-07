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
Definition of ListNode
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: l1: ListNode l1 is the head of the linked list
    @param: l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        
        if l1 == None and l2 == None:
            return None
        elif l1 == None and l2 != None:
            head = ListNode(l2.val)
            l2 = l2.next
        elif l1 != None and l2 == None:
            head = ListNode(l1.val)
            l1 = l1.next
        else:
            if l1.val < l2.val:
                head =  ListNode(l1.val)
                l1 = l1.next
            else:
                head = ListNode(l2.val)
                l2 = l2.next
    
        l = head

        while l1 != None or l2 != None:
            if l1 != None and l2 != None:
                if l1.val < l2.val:
                    l.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    l.next = ListNode(l2.val)
                    l2 = l2.next
                l = l.next
            elif l1 != None and l2 == None:
                l.next = ListNode(l1.val)
                l1 = l1.next
                l = l.next
            else:
                l.next = ListNode(l2.val)
                l2 = l2.next
                l = l.next

        return head

if __name__ == '__main__':
    l1 = ListNode(0)
    l1.next = ListNode(3)
    l1.next.next = ListNode(3)

    l2 = None

    s = Solution()
    l = s.mergeTwoLists(l1, l2)

    while l != None:
        print l.val
        l = l.next
