#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20181230
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
    @param head: a singly linked list
    @return: Modified linked list
    """
    def oddEvenList(self, head):
        # write your code here
        if head and not head.next:
            return head

        h1 = head
        h2 = head.next
        h3 = head.next
        
        while h1 and h2:
            h1.next = h2.next
            if h1.next:
                h1 = h1.next
                h2.next = h1.next
                h2 = h2.next
            else:
                h2.next = None
                h2 = h2.next
        h1.next = h3
        return head

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    obj = Solution()
    head = obj.oddEvenList(head)
    while head:
        print(head.val)
        head = head.next
